"""CDES-C Core Models - Commerce data models for cannabis retail."""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, date
from decimal import Decimal
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

class ProductStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DISCONTINUED = "discontinued"
    OUT_OF_STOCK = "out_of_stock"
    PENDING_APPROVAL = "pending_approval"

class OrderStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    ACKNOWLEDGED = "acknowledged"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class FulfillmentStatus(str, Enum):
    PENDING = "pending"
    PARTIAL = "partial"
    COMPLETE = "complete"
    CANCELLED = "cancelled"

class PriceType(str, Enum):
    RETAIL = "retail"
    WHOLESALE = "wholesale"
    MEDICAL = "medical"
    RECREATIONAL = "recreational"
    MEMBER = "member"
    SALE = "sale"

class TaxCategory(str, Enum):
    STANDARD = "standard"
    MEDICAL_EXEMPT = "medical_exempt"
    REDUCED = "reduced"
    ZERO_RATED = "zero_rated"

class UnitOfMeasure(str, Enum):
    EACH = "each"
    GRAM = "gram"
    OUNCE = "ounce"
    MILLIGRAM = "milligram"
    MILLILITER = "milliliter"
    PACK = "pack"

class ProductCategory(str, Enum):
    FLOWER = "flower"
    PREROLL = "preroll"
    VAPE = "vape"
    CONCENTRATE = "concentrate"
    EDIBLE = "edible"
    TINCTURE = "tincture"
    TOPICAL = "topical"
    CAPSULE = "capsule"
    ACCESSORY = "accessory"

@dataclass
class Price:
    amount: Decimal = Decimal("0.00")
    currency: str = "USD"
    price_type: PriceType = PriceType.RETAIL
    min_quantity: int = 1
    valid_from: Optional[datetime] = None
    valid_until: Optional[datetime] = None

@dataclass
class Discount:
    name: str = ""
    discount_type: str = "percentage"
    value: Decimal = Decimal("0.00")
    promo_code: Optional[str] = None
    min_quantity: Optional[int] = None
    valid_from: Optional[datetime] = None
    valid_until: Optional[datetime] = None

@dataclass
class ProductVariant:
    id: UUID = field(default_factory=uuid4)
    sku: str = ""
    name: str = ""
    gtin: Optional[str] = None
    weight_grams: Optional[Decimal] = None
    thc_mg: Optional[Decimal] = None
    cbd_mg: Optional[Decimal] = None
    prices: list[Price] = field(default_factory=list)

@dataclass
class CannabisProduct:
    id: UUID = field(default_factory=uuid4)
    sku: str = ""
    gtin: Optional[str] = None
    name: str = ""
    description: Optional[str] = None
    brand: Optional[str] = None
    category: ProductCategory = ProductCategory.FLOWER
    strain_name: Optional[str] = None
    strain_type: Optional[str] = None
    thc_percentage: Optional[Decimal] = None
    cbd_percentage: Optional[Decimal] = None
    batch_number: Optional[str] = None
    coa_url: Optional[str] = None
    status: ProductStatus = ProductStatus.ACTIVE
    variants: list[ProductVariant] = field(default_factory=list)
    prices: list[Price] = field(default_factory=list)
    discounts: list[Discount] = field(default_factory=list)
    tax_category: TaxCategory = TaxCategory.STANDARD
    unit_of_measure: UnitOfMeasure = UnitOfMeasure.EACH
    image_urls: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class ProductCatalog:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    supplier_gln: Optional[str] = None
    products: list[CannabisProduct] = field(default_factory=list)
    valid_from: Optional[datetime] = None
    valid_until: Optional[datetime] = None
    version: str = "1.0"
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class PurchaseOrderLine:
    line_number: int = 1
    product_id: Optional[UUID] = None
    sku: str = ""
    gtin: Optional[str] = None
    description: str = ""
    quantity_ordered: int = 0
    unit_of_measure: UnitOfMeasure = UnitOfMeasure.EACH
    unit_price: Decimal = Decimal("0.00")
    line_total: Decimal = Decimal("0.00")

@dataclass
class PurchaseOrder:
    id: UUID = field(default_factory=uuid4)
    po_number: str = ""
    buyer_gln: Optional[str] = None
    seller_gln: Optional[str] = None
    status: OrderStatus = OrderStatus.DRAFT
    lines: list[PurchaseOrderLine] = field(default_factory=list)
    subtotal: Decimal = Decimal("0.00")
    tax_total: Decimal = Decimal("0.00")
    total: Decimal = Decimal("0.00")
    order_date: datetime = field(default_factory=datetime.utcnow)
    requested_delivery_date: Optional[date] = None
    ship_to_location: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class OrderAcknowledgment:
    id: UUID = field(default_factory=uuid4)
    po_number: str = ""
    ack_number: str = ""
    status: str = "accepted"
    lines_accepted: int = 0
    lines_rejected: int = 0
    estimated_ship_date: Optional[date] = None
    notes: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class AdvanceShipNotice:
    id: UUID = field(default_factory=uuid4)
    asn_number: str = ""
    po_number: str = ""
    sscc: Optional[str] = None
    carrier: Optional[str] = None
    tracking_number: Optional[str] = None
    ship_date: date = field(default_factory=date.today)
    estimated_delivery_date: Optional[date] = None
    lines: list[PurchaseOrderLine] = field(default_factory=list)
    total_weight_kg: Optional[Decimal] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Invoice:
    id: UUID = field(default_factory=uuid4)
    invoice_number: str = ""
    po_number: str = ""
    buyer_gln: Optional[str] = None
    seller_gln: Optional[str] = None
    lines: list[PurchaseOrderLine] = field(default_factory=list)
    subtotal: Decimal = Decimal("0.00")
    tax_total: Decimal = Decimal("0.00")
    total: Decimal = Decimal("0.00")
    invoice_date: date = field(default_factory=date.today)
    due_date: Optional[date] = None
    payment_terms: str = "NET30"
    status: str = "pending"
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class InventoryLocation:
    id: UUID = field(default_factory=uuid4)
    gln: Optional[str] = None
    name: str = ""
    address: Optional[str] = None
    location_type: str = "warehouse"
    license_number: Optional[str] = None

@dataclass
class InventoryItem:
    id: UUID = field(default_factory=uuid4)
    product_id: UUID = field(default_factory=uuid4)
    location_id: UUID = field(default_factory=uuid4)
    sku: str = ""
    batch_number: Optional[str] = None
    quantity_on_hand: int = 0
    quantity_reserved: int = 0
    quantity_available: int = 0
    reorder_point: int = 0
    reorder_quantity: int = 0
    last_counted_at: Optional[datetime] = None
    updated_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class StockMovement:
    id: UUID = field(default_factory=uuid4)
    product_id: UUID = field(default_factory=uuid4)
    from_location_id: Optional[UUID] = None
    to_location_id: Optional[UUID] = None
    quantity: int = 0
    movement_type: str = "transfer"
    reference_number: Optional[str] = None
    batch_number: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class LicenseInfo:
    license_number: str = ""
    license_type: str = ""
    state: str = ""
    issued_date: Optional[date] = None
    expiration_date: Optional[date] = None
    is_valid: bool = True

@dataclass
class ComplianceDocument:
    id: UUID = field(default_factory=uuid4)
    document_type: str = ""
    document_number: str = ""
    product_id: Optional[UUID] = None
    batch_number: Optional[str] = None
    document_url: Optional[str] = None
    issued_date: Optional[date] = None
    expiration_date: Optional[date] = None
    verified: bool = False

@dataclass
class ChainOfCustody:
    id: UUID = field(default_factory=uuid4)
    batch_number: str = ""
    events: list[dict] = field(default_factory=list)
    current_holder_gln: Optional[str] = None
    origin_license: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

__all__ = [
    "ProductStatus", "OrderStatus", "FulfillmentStatus", "PriceType",
    "TaxCategory", "UnitOfMeasure", "ProductCategory",
    "Price", "Discount", "ProductVariant", "CannabisProduct", "ProductCatalog",
    "PurchaseOrderLine", "PurchaseOrder", "OrderAcknowledgment", "AdvanceShipNotice", "Invoice",
    "InventoryLocation", "InventoryItem", "StockMovement",
    "LicenseInfo", "ComplianceDocument", "ChainOfCustody",
]
