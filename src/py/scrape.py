import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import glob
import difflib

def extract_text_from_url(url: str)-> str:
    # URLからHTMLを取得
    response = requests.get(url)
    html_content = response.text

    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html_content, "html.parser")

    # 記事の本文を取得
    # sectionタグでidがchangelogである要素を取得
    target_elements = soup.find_all('section', id='changelog')

    # テキストを取得
    if target_elements:
        text = ''.join([element.get_text() for element in target_elements])
        # print(text)
    else:
        print("指定の要素が見つかりませんでした。")

    return text


def write_text_to_file(text: str, file_path: str):
    try:
        with open(file_path,"w", encoding='utf-8') as f:
            f.write(text)
        
    except Exception as e:
        print(f"Failed to write to file: {e}")
        

def get_formatted_current_time(format: str):
    # 現在の日時を取得
    now = datetime.now()
    # 指定のフォーマット (YYMMDDHHMMSS) で文字列に変換
    formatted_time = now.strftime(format)
    return formatted_time


def get_diff_text(target_dir: str) -> str:
    formatted_time = get_formatted_current_time('%Y/%m/%d %H:%M:%S')
    text_files = glob.glob(os.path.join(target_dir, '*.txt'))
    if len(text_files) <= 1:
        return f"{formatted_time} No change"
    # ファイルの作成日時順に並び替え
    text_files.sort(key=os.path.getctime, reverse=True)
    
    latest_text_file = text_files[0]
    prev_text_file = text_files[1]
    
    # 差分を取得
    with open(latest_text_file, encoding='utf-8') as f:
        latest_text = f.read()
    with open(prev_text_file, encoding='utf-8') as f:
        prev_text = f.read()
    
    # 同一の場合はreturn 
    if latest_text == prev_text:
        return f"{formatted_time} No change"
    
    res = difflib.ndiff(latest_text.split(), prev_text.split())
    diff = [formatted_time]
    for r in res:
        if r[0:1] in ['+', '-']:
            diff.append(r)
    diff_text = "\n".join(diff)
    
    return diff_text