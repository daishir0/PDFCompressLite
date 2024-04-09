import subprocess
import glob
import os
import sys

def compress_pdf(gs_path, input_pdf_path, output_pdf_path):
    # Ghostscriptコマンドを構築
    gs_command = [
        gs_path,
        '-sDEVICE=pdfwrite',
        '-dPDFSETTINGS=/screen',
        '-dBATCH',
        '-dNOPAUSE',
        '-dQUIET',  # GhostscriptのGUI画面を出さない
        '-dSAFER',
        f'-sOutputFile={output_pdf_path}',
        input_pdf_path
    ]

    # Ghostscriptコマンドを実行
    subprocess.run(gs_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("使用法: python compress_pdf.py <PDFディレクトリのパス>")
        sys.exit(1)

    input_dir = sys.argv[1]
    gs_path = r"C:\Program Files\gs\gs10.03.0\bin\gswin64.exe"

    # ディレクトリ内のPDFファイルを取得
    files = glob.glob(os.path.join(input_dir, "*.pdf"))

    for file in files:
        file_size = os.path.getsize(file)
        # ファイルサイズが9.8MBより大きいかどうかを確認
        if file_size > 9.8 * 1024 * 1024:
            print(f"Processing: {os.path.basename(file)}")
            outfile_name = file.replace('.pdf', '_compressed.pdf')
            
            try:
                compress_pdf(gs_path, file, outfile_name)
                print(f"Compressed PDF saved to: {outfile_name}")
            except subprocess.CalledProcessError as e:
                print(f"Error compressing PDF: {e}")
        else:
            print(f"Skipped (File size is under 9.8MB): {os.path.basename(file)}")
