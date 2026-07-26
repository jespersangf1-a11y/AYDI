"""Single source of truth for brand-reference visibility (pillar 4, stage 2).

Both the CRUD endpoints (competitors.py) and the brand_dna ANALYSIS loader
(layouts.py) must apply the SAME tenancy rule — otherwise the analysis path
leaks another org's private brand DNA back through its warnings (topology /
proportion signatures). Keeping the predicate here prevents that drift.
"""
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import BrandReferenceModel, OrganizationMember, User


async def get_my_org_ids(user: User, db: AsyncSession) -> list:
    result = await db.execute(
        select(OrganizationMember.organization_id).where(
            OrganizationMember.user_id == user.id
        )
    )
    return [row[0] for row in result.all()]


def can_see_brand_ref(ref: BrandReferenceModel, user: User, my_org_ids: list) -> bool:
    """Visibility rule:
    - org rows        -> only members of that org
    - personal rows   -> creator (or platform admin)
    - legacy/seed rows (org_id AND created_by both NULL) -> globally readable
      (they feed every user's brand_dna analysis as shared reference data)
    """
    if ref.org_id is not None:
        return ref.org_id in my_org_ids
    if ref.created_by_user_id is not None:
        return ref.created_by_user_id == user.id or user.role == "admin"
    return True  # legacy/seed
