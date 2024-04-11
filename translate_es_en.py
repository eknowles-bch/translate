import argparse
import pandas as pd
from deep_translator import GoogleTranslator
from tqdm import tqdm


def translate_column(dataframe, column_name, target_language="es"):
    translator = GoogleTranslator(source='auto', target=target_language)

    tqdm.pandas(desc=f"Translating '{column_name}'")
    return dataframe[column_name].progress_apply(lambda text: translator.translate(text) if pd.notnull(text) else text)


def main():
    parser = argparse.ArgumentParser(description='Translate columns in a CSV file.')
    parser.add_argument('csv_file', help='Path to the input CSV file')
    parser.add_argument('columns', nargs='+', help='Names of the columns to translate')
    parser.add_argument('--target_language', default='en', help='Target language for translation (default: en)')

    args = parser.parse_args()

    df = pd.read_csv(args.csv_file)

    for column_name in args.columns:
        df[column_name] = translate_column(df, column_name, args.target_language)

    output_file = args.csv_file.rsplit('.', 1)[0] + '_translated.csv'
    df.to_csv(output_file, index=False)
    print(f"Translated file saved as {output_file}")


if __name__ == "__main__":
    main()