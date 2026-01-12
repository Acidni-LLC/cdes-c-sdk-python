"""
CDES-C: Cannabis Data Exchange Standard - Commerce Extension

Enterprise commerce SDK for cannabis retail integration.
Supports GS1 identifiers, EDI X12 documents, POS systems,
and e-commerce platforms.

Integrations:
- GS1: GTIN, GLN, SSCC, DataMatrix barcodes
- EDI: X12 850 (PO), 855 (POA), 856 (ASN), 810 (Invoice)
- POS: Square, Dutchie, Treez, Flowhub
- E-commerce: Shopify, WooCommerce, BigCommerce, Magento
"""

__version__ = "0.1.0"
__author__ = "Acidni LLC"

from cdes_c.models import (
    # Enums
    ProductStatus,
    OrderStatus,
    FulfillmentStatus,
    PriceType,
    TaxCategory,
    UnitOfMeasure,
    ProductCategory,
    # Product Models
    Price,
    Discount,
    ProductVariant,
    CannabisProduct,
    ProductCatalog,
    # Order Models
    PurchaseOrderLine,
    PurchaseOrder,
    OrderAcknowledgment,
    AdvanceShipNotice,
    Invoice,
    # Inventory Models
    InventoryLocation,
    InventoryItem,
    StockMovement,
    # Compliance Models
    LicenseInfo,
    ComplianceDocument,
    ChainOfCustody,
)

__all__ = [
    "__version__",
    # Enums
    "ProductStatus",
    "OrderStatus",
    "FulfillmentStatus",
    "PriceType",
    "TaxCategory",
    "UnitOfMeasure",
    "ProductCategory",
    # Product Models
    "Price",
    "Discount",
    "ProductVariant",
    "CannabisProduct",
    "ProductCatalog",
    # Order Models
    "PurchaseOrderLine",
    "PurchaseOrder",
    "OrderAcknowledgment",
    "AdvanceShipNotice",
    "Invoice",
    # Inventory Models
    "InventoryLocation",
    "InventoryItem",
    "StockMovement",
    # Compliance Models
    "LicenseInfo",
    "ComplianceDocument",
    "ChainOfCustody",
]
