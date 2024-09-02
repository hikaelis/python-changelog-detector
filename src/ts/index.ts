import { relayURLs } from "./config";
import { composeMetadata, postToRelays } from "./postToRelays";
import { readDiffText } from "./readTextFile";


/**
 * メイン関数
 */
const main = async() => {
	// 発言内容生成
	const message = await readDiffText();
	const metadata = await composeMetadata(message);

	//投稿
	if (message != "" && metadata){
		for (const relayURL of relayURLs) {
			try {
				await postToRelays(relayURL, metadata);
			} catch (e) {
					console.log(e);
					continue;
			}
		}
	}
	console.log(`***投稿完了 「${message}」***`);


}


main().finally(() => {process.exit(0);})