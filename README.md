# CDES-C: Cannabis Data Exchange Standard - Commerce Extension

Enterprise commerce SDK for cannabis retail integration. Part of the [CDES](https://cdes.dev) ecosystem.

## Features

- **GS1 Standards** - GTIN, GLN, SSCC, DataMatrix barcodes
- **EDI X12** - Purchase orders (850), acknowledgments (855), ASN (856), invoices (810)
- **Product Catalog** - Cannabis product management with COA links
- **Inventory** - Real-time stock tracking and movements
- **Compliance** - License verification, chain of custody

## Platform Integrations

| Platform | Type | Status |
|----------|------|--------|
| Shopify | E-commerce |  Coming |
| WooCommerce | E-commerce |  Coming |
| BigCommerce | E-commerce |  Coming |
| Square | POS |  Coming |
| Dutchie | Cannabis POS |  Coming |
| Treez | Cannabis POS |  Coming |

## Installation

```bash
pip install cdes-c
```

## Quick Start

```python
from cdes_c import CannabisProduct, PurchaseOrder, ProductCategory
from cdes_c.gs1 import GTINManager

# Create a product with GS1 identifiers
product = CannabisProduct(
    sku="FL-OG-3.5",
    gtin=GTINManager.generate_gtin14("0012345"),
    name="OG Kush - 3.5g",
    category=ProductCategory.FLOWER,
    strain_name="OG Kush",
    thc_percentage=Decimal("24.5"),
    coa_url="https://lab.example.com/coa/12345"
)

# Create a purchase order
po = PurchaseOrder(
    po_number="PO-2026-001",
    buyer_gln="0012345000001",
    seller_gln="0098765000001"
)
```

## Documentation

- [Full Documentation](https://cdes.dev/docs/commerce)
- [GS1 Integration Guide](https://cdes.dev/guides/gs1)
- [EDI Implementation](https://cdes.dev/guides/edi)

## License

MIT License - see [LICENSE](LICENSE) for details.
