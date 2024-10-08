from scrape import extract_text_from_url, write_text_to_file, get_formatted_current_time, get_diff_text

def main():
    # 最新のchangelogを取得
    url = "https://docs.python.org/3/whatsnew/changelog.html"
    text = extract_text_from_url(url)
    # テキストファイルに書き込み
    formatted_time = get_formatted_current_time('%y%m%d%H%M%S')
    file_path = f"./text/changelog_text/{formatted_time}_changelog.txt"
    write_text_to_file(text, file_path)
    
    # diffを取得
    target_dir = "./text/changelog_text"
    diff_text = get_diff_text(target_dir)
    # テキストファイルに書き込み
    diff_file_path = f"./text/diff_text/diff.txt"
    write_text_to_file(diff_text, diff_file_path)
    
main()