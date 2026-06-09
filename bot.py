# tg_encrypt_bot.py
# Owner: @UnknownGuy9876 | Channel: @SGCodexs
# DEVILS WILL RISE - Telegram Encryption Bot (30+ Layers)

import logging
import base64
import urllib.parse
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# ========== CONFIG ==========
BOT_TOKEN = "8735707765:AAELATdZIyvOka_RIakWl6-uLCi2FICDjfs"  # YAHAN APNA TOKEN DAAL
# ============================

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class DevilsEncryptor:
    """30+ Layers Encryption Engine"""
    
    @staticmethod
    def base64_encode(text):
        return base64.b64encode(text.encode()).decode()
    
    @staticmethod
    def base32_encode(text):
        return base64.b32encode(text.encode()).decode()
    
    @staticmethod
    def base16_encode(text):
        return base64.b16encode(text.encode()).decode()
    
    @staticmethod
    def base85_encode(text):
        return base64.b85encode(text.encode()).decode()
    
    @staticmethod
    def url_encode(text):
        return urllib.parse.quote(text)
    
    @staticmethod
    def url_encode_plus(text):
        return urllib.parse.quote_plus(text)
    
    @staticmethod
    def hex_encode(text):
        return text.encode().hex()
    
    @staticmethod
    def reverse_string(text):
        return text[::-1]
    
    @staticmethod
    def rot13_encode(text):
        return text.translate(str.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
        ))
    
    @staticmethod
    def rot47_encode(text):
        result = []
        for c in text:
            if 33 <= ord(c) <= 126:
                result.append(chr(33 + ((ord(c) - 33 + 47) % 94)))
            else:
                result.append(c)
        return ''.join(result)
    
    @staticmethod
    def binary_encode(text):
        return ' '.join(format(ord(c), '08b') for c in text)
    
    @staticmethod
    def atbash_encode(text):
        result = []
        for c in text:
            if 'a' <= c <= 'z':
                result.append(chr(219 - ord(c)))
            elif 'A' <= c <= 'Z':
                result.append(chr(155 - ord(c)))
            else:
                result.append(c)
        return ''.join(result)
    
    @staticmethod
    def xor_encode(text, key=42):
        return ''.join(chr(ord(c) ^ key) for c in text)
    
    @staticmethod
    def caesar_encode(text, shift=5):
        result = []
        for c in text:
            if c.isupper():
                result.append(chr((ord(c) - 65 + shift) % 26 + 65))
            elif c.islower():
                result.append(chr((ord(c) - 97 + shift) % 26 + 97))
            else:
                result.append(c)
        return ''.join(result)
    
    @staticmethod
    def unicode_escape_encode(text):
        return text.encode('unicode-escape').decode()
    
    @staticmethod
    def string_escape_encode(text):
        return repr(text)[1:-1]
    
    @staticmethod
    def double_base64(text):
        return base64.b64encode(base64.b64encode(text.encode())).decode()
    
    @staticmethod
    def base64_then_hex(text):
        return base64.b64encode(text.encode()).hex()
    
    @staticmethod
    def hex_then_base64(text):
        return base64.b64encode(text.encode().hex().encode()).decode()
    
    def encrypt_multi_layer(self, text, layers=30):
        """Apply random 30+ encryption layers"""
        encoders = [
            self.base64_encode, self.base32_encode, self.base16_encode,
            self.base85_encode, self.url_encode, self.url_encode_plus,
            self.hex_encode, self.reverse_string, self.rot13_encode,
            self.rot47_encode, self.binary_encode, self.atbash_encode,
            self.unicode_escape_encode, self.string_escape_encode,
            self.double_base64, self.base64_then_hex, self.hex_then_base64
        ]
        
        current = text
        applied_layers = []
        
        # XOR aur Caesar ke liye random keys
        xors = [self.xor_encode]
        caesars = [self.caesar_encode]
        
        all_encoders = encoders + xors + caesars
        
        for i in range(layers):
            encoder = random.choice(all_encoders)
            try:
                if encoder.__name__ == 'xor_encode':
                    key = random.randint(1, 255)
                    current = encoder(current, key)
                    applied_layers.append(f"XOR(key={key})")
                elif encoder.__name__ == 'caesar_encode':
                    shift = random.randint(1, 25)
                    current = encoder(current, shift)
                    applied_layers.append(f"Caesar(shift={shift})")
                else:
                    current = encoder(current)
                    applied_layers.append(encoder.__name__)
            except:
                continue
        
        return current, len(applied_layers), applied_layers

encryptor = DevilsEncryptor()

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "💀 **DEVILS WILL RISE - ENCRYPTION BOT** 💀\n\n"
        "Send me any text or file.\n"
        "I will encrypt it with **30+ layers**!\n\n"
        "Commands:\n"
        "/encrypt <text> - Encrypt text\n"
        "/layers - Show available layers\n"
        "/about - Bot info",
        parse_mode='Markdown'
    )

async def encrypt_command(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("Usage: /encrypt <your text>")
        return
    
    text = ' '.join(context.args)
    await update.message.reply_chat_action(action="typing")
    
    encrypted, layers, applied = encryptor.encrypt_multi_layer(text, layers=30)
    
    response = f"✅ **Encryption Complete!**\n📊 **Layers applied:** {layers}\n\n"
    response += f"```\n{encrypted[:1500]}\n```"
    
    if len(encrypted) > 1500:
        response += f"\n⚠️ Output truncated. Full: {len(encrypted)} chars"
    
    await update.message.reply_text(response, parse_mode='Markdown')
    
    # Send as file if too long
    if len(encrypted) > 2000:
        with open("encrypted_output.txt", "w") as f:
            f.write(encrypted)
        await update.message.reply_document(document=open("encrypted_output.txt", "rb"))

async def layers_command(update: Update, context: CallbackContext):
    text = """
📖 **Available Encryption Layers (30+)**

**Encoding:**
• Base64, Base32, Base16, Base85
• URL Encoding, URL+ Encoding
• Hex Encoding
• Binary Encoding

**Ciphers:**
• ROT13, ROT47
• Atbash Cipher
• Reverse String
• XOR (random key 1-255)
• Caesar (random shift 1-25)

**Combos:**
• Unicode Escape
• String Escape
• Double Base64
• Base64 → Hex
• Hex → Base64

**Features:**
✅ Random layer selection
✅ 30+ layers automatically
✅ Recursive encryption
✅ File support coming soon
"""
    await update.message.reply_text(text)

async def about_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🤖 **DEVILS WILL RISE - ENCRYPTION BOT**\n\n"
        "Creator: @UnknownGuy9876\n"
        "Channel: @SGCodexs\n"
        "Version: 2.0\n\n"
        "Encrypts text with 30+ layers.\n"
        "Use /encrypt <text> to start.\n\n"
        "⚠️ Keep your decryption bot handy!",
        parse_mode='Markdown'
    )

async def handle_text(update: Update, context: CallbackContext):
    # Auto-encrypt any text sent
    text = update.message.text
    if text.startswith('/'):
        return
    
    await update.message.reply_chat_action(action="typing")
    encrypted, layers, _ = encryptor.encrypt_multi_layer(text, layers=30)
    
    await update.message.reply_text(
        f"🔒 **Encrypted ({layers} layers)**\n\n```\n{encrypted[:1000]}\n```",
        parse_mode='Markdown'
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("encrypt", encrypt_command))
    app.add_handler(CommandHandler("layers", layers_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    print("💀 DEVILS WILL RISE - ENCRYPTION BOT STARTED 💀")
    print(f"Owner: @UnknownGuy9876 | Channel: @SGCodexs")
    
    app.run_polling()

if __name__ == "__main__":
    main()
