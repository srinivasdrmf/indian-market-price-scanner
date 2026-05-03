#!/usr/bin/env python3
"""
Indian Market Price Scanner
Monitor all major Indian e-commerce platforms for items below 80% of original price
"""

import logging
import yaml
from scanner.core import PriceScanner

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    """Main entry point"""
    
    # Load configuration
    try:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error('config.yaml not found. Please create configuration file.')
        return
    
    # Product keywords to search
    product_keywords = [
        'laptop', 'smartphone', 'headphones', 'smartwatch',
        'wireless earbuds', 'power bank', 'monitor',
        'keyboard', 'mouse', 'gaming console'
    ]
    
    # Initialize scanner
    scanner = PriceScanner(config, discount_threshold=0.80)
    
    # Scan all marketplaces
    print("\n🔍 Starting Indian Market Price Scanner...")
    print("=" * 80)
    
    results = scanner.scan_all_marketplaces(product_keywords)
    
    # Print summary
    scanner.print_summary()
    
    # Generate reports
    csv_path, json_path = scanner.generate_reports()
    
    print(f"\n✅ Scan complete!")
    print(f"📊 Reports saved to:")
    print(f"   • CSV: {csv_path}")
    print(f"   • JSON: {json_path}")
    print("=" * 80 + "\n")

if __name__ == '__main__':
    main()
