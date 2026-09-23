# Keyboard Auto Input

這個專案是一個簡單的 Python 自動鍵盤輸入範例，用來模擬按鍵操作與自動輸入字串。它主要透過 `pyautogui` 來執行以下動作：

- 按下 `Alt + Tab` 切換到目標視窗
- 自動輸入指定指令
- 按下 `Enter` 執行

目前範例中，程式會輸入一段類似 `nikto` 的命令字串，方便用於測試或快速自動化輸入場景。

## 專案簡介

這個專案適合用於：

- 自動化測試的小型腳本
- 快速模擬鍵盤輸入
- 將命令字串送到前景視窗
- 學習 Python GUI 自動化基礎

## 專案結構

```text
keyboard-auto-input/
├── main.py
├── Keybord_auto_input/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
└── README.md
```

## 需求

- Python 3.x
- `pyautogui`

## 安裝步驟

1. Clone 專案：

```bash
git clone https://github.com/jason22432150/keyboard-auto-input.git
cd keyboard-auto-input
```

2. 建立虛擬環境（可選）：

```bash
python -m venv Keybord_auto_input
```

3. 啟用虛擬環境：

- Windows:

```bash
Keybord_auto_input\Scripts\activate
```

- macOS / Linux:

```bash
source Keybord_auto_input/bin/activate
```

4. 安裝依賴：

```bash
pip install pyautogui
```

## 執行方式

在專案根目錄執行：

```bash
python main.py
```

## 目前程式行為

`main.py` 目前會：

1. 按下 `Alt + Tab`
2. 輸入：

```text
./nikto.pl -h http://www.example.com
```

3. 按下 `Enter`

這代表它會在前景視窗中模擬鍵盤輸入命令，適合用於自動化操作桌面應用程式或終端機。

## 注意事項

- 這種腳本會操作滑鼠與鍵盤，請在可控的環境中執行。
- 需要讓目標視窗位於前景，否則 `pyautogui` 可能無法正確輸入。
- 在某些作業系統或桌面環境中，可能需要授權或調整權限。
- 不建議用於未經授權的自動化操作。

## 範例程式碼

```python
import pyautogui

pyautogui.keyDown("alt")
pyautogui.keyDown("tab")

pyautogui.keyUp("alt")
pyautogui.keyUp("tab")

str = "./nikto.pl -h http://www.example.com"
pyautogui.write(str)

pyautogui.keyDown("enter")
pyautogui.keyUp("enter")
```

## 授權

本專案目前未明確宣告授權條款，若需公開使用，建議視情況補上 `LICENSE` 檔案。

## 補充

如果你想要擴充這個專案，未來可以加入：

- 可自訂輸入內容
- 可讀取外部設定檔
- 可支援多個命令序列
- 支援 Windows / Linux / macOS 差異處理

這個專案是一個很適合入門的 Python 鍵盤自動化例子，適合用來學習 `pyautogui` 的基本用法。
