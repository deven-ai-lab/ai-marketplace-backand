from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, text
from typing import List, Optional
import uuid
from datetime import datetime
from pydantic import BaseModel
from config import engine, SessionLocal, get_db, HOST, PORT, DEBUG
from models import Base, Brand, Creator, Campaign

app = FastAPI(title="AI-to-AI Marketplace API", version="1.0.0")

# ========== PYDANTIC SCHEMAS ==========

class BrandCreate(BaseModel):
    name: str
    industry: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    budget: Optional[float] = None
    target_audience_age: Optional[str] = None
    target_audience_interests: Optional[str] = None
    target_audience_gender: Optional[str] = None
    platforms_needed: Optional[List[str]] = None
    content_format_wanted: Optional[List[str]] = None
    content_type: Optional[List[str]] = None
    location_geography_focus: Optional[str] = None
    timeline: Optional[str] = None
    brand_brief: Optional[str] = None
    past_campaigns_links: Optional[List[str]] = None
    deven_notes: Optional[str] = None

class BrandResponse(BrandCreate):
    id: uuid.UUID
    status: str
    stage: str
    matched_creators: Optional[List[uuid.UUID]] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CreatorCreate(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    instagram_handle: Optional[str] = None
    youtube_channel: Optional[str] = None
    tiktok_handle: Optional[str] = None
    other_platforms: Optional[dict] = None
    follower_count_instagram: Optional[float] = None
    follower_count_youtube: Optional[float] = None
    follower_count_tiktok: Optional[float] = None
    engagement_rate: Optional[float] = None
    niche: Optional[str] = None
    content_specialties: Optional[List[str]] = None
    audience_age: Optional[str] = None
    audience_gender: Optional[str] = None
    location: Optional[str] = None
    rates_per_post: Optional[float] = None
    rates_per_story: Optional[float] = None
    rates_per_reel: Optional[float] = None
    rates_longform_video: Optional[float] = None
    barter_willing: Optional[bool] = False
    past_brand_collaborations: Optional[List[str]] = None
    bio: Optional[str] = None
    profile_picture_url: Optional[str] = None
    deven_notes: Optional[str] = None

class CreatorResponse(CreatorCreate):
    id: uuid.UUID
    availability_status: str
    created_at: datetime
    updated_at: datetime

    class Config:
