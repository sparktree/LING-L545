## Maxmatch performance
___

Below is a histogram of the sentences' WER.

![WER Histogram](werHist.png)

The maxmatch program gave a result of an average WER of 34.92%, with the median WER being 33.91%. The sentence with the closest WER to the mean is here, with 34.88%:  

WER: 34.88%  
REF: 可能 這 就是 為 什麼 當 飛 逝  的 時間 揭 示  了 他 的 成果 ， 揭 示  了 他 對 結 合 水   的 秘密 的 發現 時 ， 洶 湧  的 眼 淚  模糊 了 他 的 眼 睛  。   
HYP: 可能 這 就是 為 什麼 當   飛逝 的 時間   揭示 了 他 的 成果 ，   揭示 了 他 對     結合水 的 秘密 的 發現 時 ，   洶湧 的   眼淚 模糊 了 他 的   眼睛 。   
EVA:                D S       D S             D S        D D S                 D S    D S           D S

We can see that the primary problem is the lack of words in the dictionary to match to, with many words being separated out into single characters, such as with 飛 逝 versus 飛逝. Punctuation and dictionary findings are properly dealt with. Through the 200 sentences, only 6 times did two unrelated words get tokenized together, all of which involve at least one of the words having just one symbol. Here is such an example:

WER: 61.76%  
REF: 和 許多 社會 主義者   一樣 ， P e d r o S á n c h e     z       在 É v o l e     項目 中 表示 西班牙 是 萬 民  之 邦 。   
HYP: 和 許多 社會 主義  者 一樣 ，                     Pedro Sánchez 在         Évole 項目 中 表示 西班牙 是   萬民 之 邦 。   
EVA:         S   I      D D D D D D D D D D S     S         D D D D S                   D S   

We can see that 主義者 was formed when the final 者 symbol is meant to be a separate token. However, this sentence also displays a larger issue that accounts for much of the WER through the data. The Latin character names tested on are not present within the training dictionaries, so each character within these names gets spaced out and causes large strings of errors within the tokenizing process. Here is the highest WER sentence, and the one with the seemingly most egregious case of name spacing:
    
WER: 81.36%  
REF: G of f r e d o P e t r a s s        i        的 兩 個 學生 、 E n n i o M o r r i c o n     e         以及 B r u n o N i c o l a     i       在 聖 塞 西 莉 亞     音樂 學校 見 面  了 。   
HYP:                            Goffredo Petrassi 的 兩 個 學生 、                         Ennio Morricone 以及                     Bruno Nicolai 在         聖塞西莉亞 音樂 學校   見面 了 。  
EVA: D D  D D D D D D D D D D D S        S                   D D D D D D D D D D D D S     S            D D D D D D D D D D S     S         D D D D S           D S   

Without the names, this sentence would not perform phenomenally, but it would be much better. There were 9 cases of perfectly tokenized sentences, but none exist between 0.00% and 8.33%. Here is the longest of these perfect tokenizations:

WER: 0.00%  
REF: 就 像 大 多數 南 歐 的 地點 一樣 ， 該 研究 可 追溯 到 早 至 公元 前 5 世紀 。   
HYP: 就 像 大 多數 南 歐 的 地點 一樣 ， 該 研究 可 追溯 到 早 至 公元 前 5 世紀 。   
EVA: 

And here is the 8.33% WER sentence, containing just one missed word:

WER: 8.33%  
REF: 他 也 表示 ， “ 這樣 一 份 文 件  的 存在 可能 會 帶來 讓 人 難 以 接受 的 後果 。 ”   
HYP: 他 也 表示 ， “ 這樣 一 份   文件 的 存在 可能 會 帶來 讓 人 難 以 接受 的 後果 。 ”   
EVA:                   D S 

Overall, the performance of maxmatch is quite satisfactory, considering the simplicity of the algorithm, and has potential for significant improvement when tested on data without Latin character names, or if Latin alphabet characters are simply left alone in the tokenizing process.