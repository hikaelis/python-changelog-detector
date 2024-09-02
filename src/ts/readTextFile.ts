import * as fs from "fs"

export const readDiffText = (): string => {
  const diffText = "./text/diff_text/diff.txt";
  const text = fs.readFileSync(diffText, "utf-8");
  console.log(text)
  
  return text;
}

readDiffText();