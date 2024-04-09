# PDFCompressLite

## Overview
PDFCompressLite is a command-line utility designed to compress PDF files in a specified directory that are larger than 9.8MB, using Ghostscript. It's particularly useful for reducing the file size of large PDFs for easier storage and distribution.

## Installation
1. Ensure Python is installed on your system.
2. Install Ghostscript and note the installation path.
3. Clone this repository or download the script directly.
4. Optionally, create a virtual environment and install dependencies listed in `requirements.txt`.

## Usage
Run the script from the command line, specifying the path to the directory containing the PDFs you wish to compress:
```
python compress_pdf.py <Path to PDF directory>
```
Make sure to replace `<Path to PDF directory>` with the actual path.

## Note
- The script requires the path to the Ghostscript executable to be specified within the script. Ensure this path is correctly set according to your Ghostscript installation.
- Only PDF files larger than 9.8MB will be compressed.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# PDFCompressLite

## 概要
PDFCompressLiteは、指定されたディレクトリ内の9.8MBを超えるPDFファイルをGhostscriptを使用して圧縮するコマンドラインユーティリティです。大きなPDFファイルのサイズを縮小して、保管や配布を容易にするために特に便利です。

## インストール方法
1. システムにPythonがインストールされていることを確認してください。
2. Ghostscriptをインストールし、インストールパスをメモしておきます。
3. このリポジトリをクローンするか、スクリプトを直接ダウンロードします。
4. オプションで、仮想環境を作成し、`requirements.txt`に記載されている依存関係をインストールします。

## 使い方
コマンドラインからスクリプトを実行し、圧縮したいPDFが含まれているディレクトリへのパスを指定します：
```
python compress_pdf.py <Path to PDF directory>
```
`<PDFディレクトリへのパス>`を実際のパスに置き換えてください。

## 注意点
- スクリプトはGhostscriptの実行可能ファイルへのパスがスクリプト内で指定されている必要があります。このパスは、お使いのGhostscriptのインストールに応じて正しく設定されていることを確認してください。
- 9.8MBを超えるPDFファイルのみが圧縮されます。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています - 詳細はLICENSEファイルを参照してください。
