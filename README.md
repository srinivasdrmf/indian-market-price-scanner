# Indian Market Price Scanner

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)

A powerful Python-based scanner that monitors **all major Indian e-commerce platforms** for products priced below 80% of their original price (20%+ discount) with automatic filtering, deal scoring, and comprehensive reporting.

## 🎯 Features

- **Multi-Marketplace Support**: Scans Amazon India, Flipkart, Myntra, AJIO, Nykaa, Croma, and Meesho
- **Smart Deal Detection**: Automatically identifies items with 20%+ discounts (below 80% of original price)
- **Deal Scoring**: Ranks deals by discount % + product rating for easy filtering
- **Multi-threaded Scanning**: Parallel processing across all marketplaces for fast results
- **Anti-Bot Protection**: Uses curl_cffi with TLS/JA3 fingerprinting to bypass blocks
- **Multiple Export Formats**: CSV and JSON reports for data analysis
- **Configurable**: YAML-based settings for easy customization
- **Scheduled Scanning**: Option to run on intervals (hourly, daily, etc.)
- **Detailed Logging**: Track all operations and errors

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

```bash
git clone https://github.com/srinivasdrmf/indian-market-price-scanner.git
cd indian-market-price-scanner
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

## 📋 Project Structure

```
indian-market-price-scanner/
├── main.py                    # Entry point
├── config.yaml               # Configuration file
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
├── scanner/
│   ├── __init__.py
│   ├── core.py              # Core scanner engine
│   ├── price_filter.py      # Filtering logic
│   ├── reporters.py         # Report generation (CSV/JSON)
│   └── marketplaces/        # Marketplace-specific scrapers
│       ├── __init__.py
│       ├── amazon_india.py
│       ├── flipkart.py
│       ├── myntra.py
│       ├── ajio.py
│       ├── nykaa.py
│       ├── croma.py
│       └── meesho.py
├── output/                  # Generated reports
│   ├── deals_YYYYMMDD_HHMMSS.csv
│   └── deals_YYYYMMDD_HHMMSS.json
└── logs/                    # Application logs
    └── scanner.log
```

## ⚙️ Configuration

Edit `config.yaml` to customize:

```yaml
scanner:
  discount_threshold: 0.80    # Items at 80% or less of original price
  check_interval: 3600        # Scan every hour
  timeout: 30                 # Request timeout in seconds
  max_retries: 3              # Retry failed requests

marketplaces:
  amazon_india:
    enabled: true
  flipkart:
    enabled: true
  # ... enable/disable marketplaces as needed
```

## 📊 Output

The scanner generates reports in both CSV and JSON formats:

### CSV Report
```
marketplace,product_name,brand,original_price,current_price,discount_pct,rating,deal_score
Amazon India,iPhone 13,Apple,₹79999,₹59999,25.0%,4.5,47.5
```

### JSON Report
```json
{
  "scan_timestamp": "2026-05-03T14:30:00",
  "total_deals": 156,
  "threshold": "< 80% of original price",
  "deals": [...]
}
```

## 🛍️ Supported Categories

- Electronics & Gadgets
- Fashion & Apparel
- Beauty & Cosmetics
- Home & Kitchen
- Sports & Outdoors
- Books & Media

## 🔧 Technical Stack

- **Python 3.8+**: Core language
- **Selenium**: For JavaScript-heavy sites
- **BeautifulSoup4**: HTML parsing
- **curl_cffi**: TLS fingerprinting to bypass blocks
- **Requests**: HTTP library
- **Pandas**: Data analysis
- **PyYAML**: Configuration management
- **Schedule**: Task scheduling

## 📈 Performance

- Scans 7 marketplaces in ~2-5 minutes
- Multi-threaded design for parallel processing
- Handles 100+ products per marketplace
- Respects website rate limits and robots.txt

## ⚠️ Legal & Ethical

- Respects `robots.txt` and website terms of service
- Non-commercial use only
- Follows responsible web scraping practices
- Complies with data protection regulations

## 🐛 Troubleshooting

### Issue: No results found
- Check internet connection
- Verify marketplace URLs in config.yaml
- Check if marketplaces are currently available

### Issue: Rate limiting
- Increase `check_interval` in config.yaml
- Reduce number of product keywords
- Check IP blocking status

### Issue: Import errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Use Python 3.8+ : `python --version`

## 🚀 Future Enhancements

- [ ] Real-time price notifications via email/SMS
- [ ] Historical price tracking and graphs
- [ ] AI-based deal recommendations
- [ ] Mobile app for iOS/Android
- [ ] Browser extension for Chrome/Firefox
- [ ] Database integration for long-term tracking
- [ ] Telegram/WhatsApp bot integration

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ for Indian shoppers**
