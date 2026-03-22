# AI Chat Log to Obsidian Converter

AIのチャットログを整理し、Obsidianで活用できるMarkdownノートに変換するツールです。

AIとの会話には有用な知識や技術的な情報が多く含まれていますが、チャット形式のままでは検索・整理・再利用が難しいという課題があります。
本ツールはチャットログを処理し、構造化されたMarkdownファイルに変換してObsidianのVaultに保存することで、個人のナレッジベースとして活用できるようにします。

---

## 主な機能

* AIチャットログの整理
* Markdown形式への変換
* Obsidian Vaultへの自動保存
* 日付・タイトル付きノートの生成
* 会話内容のナレッジ化

---

## 処理の流れ

```id="t0a8aj"
AIチャットログ  
↓  
テキスト処理  
↓  
Markdown変換  
↓  
Obsidian Vaultへ保存  
```

---

## 概要

本ツールは、会話形式のログを整理されたMarkdownノートへ変換します。
これにより、Obsidian上で検索・整理しやすい形で情報を管理できるようになります。

---

## 出力例

生成されるノート例：
2026-03-08 AI Conversation Topic

```id="0f9pyd"
How to retrieve weather data using Python

Notes

- Use the Japan Meteorological Agency historical data page
- Data can be downloaded in CSV format
- Python can automate the retrieval process
```

---

## 利用シーン

* AIとの会話内容の整理
* 技術メモの保存
* 学習ログの管理
* アイデアのストック

---

## 技術構成

* Python
* Markdown
* Obsidian

---

## 背景・目的

AIとの対話は有益な情報源ですが、そのままのログでは体系的な知識管理には適していません。

本プロジェクトでは、チャットログを構造化されたMarkdownノートに変換することで、AIとの対話を再利用可能なナレッジとして蓄積する仕組みを実現しました。

---

## 使い方

```id="e2ux5n"
1. ChatGPTのデータをエクスポートし、conversations.jsonを取得する
2. chat_to_obsidian.py と同じフォルダに配置する
3. スクリプトを実行する

python chat_to_obsidian.py
```

---

実行後、outputフォルダにMarkdownファイルが生成されます。

## リポジトリ構成

```
ai-chat-log-to-obsidian/
├ chat_to_obsidian.py    # チャットログをMarkdownに変換するメインスクリプト
├ README.md
└ .gitignore
```
