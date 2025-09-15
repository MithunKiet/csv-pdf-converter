import argparse
from pathlib import Path
from datetime import datetime
from .io_utils import read_csv
from .data_processing import normalize_assets
from .pdf_renderer import render_table_pdf

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    parser = argparse.ArgumentParser(description="Generate PDF report from CSV using pandas + reportlab")
    parser.add_argument("--input", "-i", required=True, help="Path to input CSV file")
    parser.add_argument("--output", "-o", help="Output PDF file path (timestamp will be added automatically)")
    parser.add_argument("--title", "-t", default="Asset Report", help="PDF title")
    args = parser.parse_args()

    # agar user output de, usme timestamp inject karo
    if args.output:
        out_path = Path(args.output)
        out_path = out_path.with_stem(out_path.stem + f"_{timestamp}")
    else:
        out_path = Path(f"report_{timestamp}.pdf")

    csv_path = Path(args.input)
    if not csv_path.exists():
        raise FileNotFoundError(f"Input file not found: {csv_path}")

    df = read_csv(csv_path)
    df = normalize_assets(df)
    render_table_pdf(df, out_path, args.title)

if __name__ == "__main__":
    main()
