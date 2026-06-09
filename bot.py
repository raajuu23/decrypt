# tg_file_encrypt_bot.py
# Owner: @UnknownGuy9876 | Channel: @SGCodexs
# DEVILS WILL RISE - File Encryption Bot (30+ Layers)

import logging
import base64
import urllib.parse
import random
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# ========== CONFIG ==========
BOT_TOKEN = "8735707765:AAELATdZIyvOka_RIakWl6-uLCi2FICDjfs"
# ============================

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class FileEncryptor:
    """30+ Layers File Encryption Engine"""
    
    @staticmethod
    def base64_encode(data):
        return base64.b64encode(data).decode()
    
    @staticmethod
    def base32_encode(data):
        return base64.b32encode(data).decode()
    
    @staticmethod
    def base16_encode(data):
        return base64.b16encode(data).decode()
    
    @staticmethod
    def base85_encode(data):
        return base64.b85encode(data).decode()
    
    @staticmethod
    def url_encode(data):
        return urllib.parse.quote(data.decode('latin-1'))
    
    @staticmethod
    def hex_encode(data):
        return data.hex()
    
    @staticmethod
    def reverse_string(data):
        return data[::-1].decode('latin-1')
    
    @staticmethod
    def rot13_encode(data):
        text = data.decode('latin-1')
        result = text.translate(str.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
        ))
        return result
    
    @staticmethod
    def rot47_encode(data):
        text = data.decode('latin-1')
        result = []
        for c in text:
            if 33 <= ord(c) <= 126:
                result.append(chr(33 + ((ord(c) - 33 + 47) % 94)))
            else:
                result.append(c)
        return ''.join(result)
    
    @staticmethod
    def binary_encode(data):
        return ' '.join(format(b, '08b') for b in data)
    
    @staticmethod
    def atbash_encode(data):
        text = data.decode('latin-1')
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
    def xor_encode(data, key=42):
        return bytes(b ^ key for b in data).decode('latin-1')
    
    @staticmethod
    def caesar_encode(data, shift=5):
        text = data.decode('latin-1')
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
    def unicode_escape_encode(data):
        return data.decode('latin-1').encode('unicode-escape').decode()
    
    @staticmethod
    def double_base64(data):
        return base64.b64encode(base64.b64encode(data)).decode()
    
    @staticmethod
    def base64_then_hex(data):
        return base64.b64encode(data).hex()
    
    @staticmethod
    def hex_then_base64(data):
        return base64.b64encode(data.hex().encode()).decode()
    
    def encrypt_file_multi_layer(self, file_data, layers=30):
        """Apply random 30+ encryption layers on file"""
        encoders = [
            self.base64_encode, self.base32_encode, self.base16_encode,
            self.base85_encode, self.url_encode, self.hex_encode,
            self.reverse_string, self.rot13_encode, self.rot47_encode,
            self.binary_encode, self.atbash_encode, self.unicode_escape_encode,
            self.double_base64, self.base64_then_hex, self.hex_then_base64
        ]
        
        # XOR aur Caesar ke liye random keys
        current = file_data
        applied_layers = []
        
        for i in range(layers):
            encoder = random.choice(encoders)
            try:
                if encoder.__name__ == 'xor_encode':
                    key = random.randint(1, 255)
                    result = encoder(current, key)
                    current = result.encode()
                    applied_layers.append(f"XOR(key={key})")
                elif encoder.__name__ == 'caesar_encode':
                    shift = random.randint(1, 25)
                    result = encoder(current, shift)
                    current = result.encode()
                    applied_layers.append(f"Caesar(shift={shift})")
                else:
                    result = encoder(current)
                    if isinstance(result, str):
                        current = result.encode()
                    else:
                        current = result
                    applied_layers.append(encoder.__name__)
            except Exception as e:
                continue
        
        return current, len(applied_layers), applied_layers

encryptor = FileEncryptor()

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "💀 **DEVILS WILL RISE - FILE ENCRYPTION BOT** 💀\n\n"
        "🔒 **Send me any .py file**\n"
        "⚡ I will encrypt it with **30+ LAYERS**\n"
        "📥 You get back encrypted file instantly\n\n"
        "**Random layers include:**\n"
        "• Base64/32/16/85 • URL/Hex • ROT13/ROT47\n"
        "• Binary/Atbash • XOR/Caesar • Double Base64\n"
        "• Unicode Escape • And many more!\n\n"
        f"**Owner:** @UnknownGuy9876\n"
        f"**Channel:** @SGCodexs\n\n"
        "🚀 Just send your .py file and watch the magic!",
        parse_mode='Markdown'
    )

async def handle_file(update: Update, context: CallbackContext):
    """Encrypt any .py file sent by user"""
    file = await update.message.document.get_file()
    
    # Check if it's a .py file
    file_name = update.message.document.file_name
    if not file_name.endswith('.py'):
        await update.message.reply_text("❌ **Sirf .py file bhejo bhai!**\n\nFiles with .py extension only.", parse_mode='Markdown')
        return
    
    # Send processing message
    msg = await update.message.reply_text(f"📀 **Encrypting** `{file_name}`\n⚡ Applying 30+ random layers...\n⏳ Please wait...", parse_mode='Markdown')
    
    # Download file
    input_path = f"temp_{update.message.document.file_id}.py"
    await file.download_to_drive(input_path)
    
    # Read file data
    with open(input_path, 'rb') as f:
        file_data = f.read()
    
    # Encrypt with 30+ layers
    encrypted_data, layers, applied = encryptor.encrypt_file_multi_layer(file_data, layers=35)
    
    # Save encrypted file
    output_name = f"encrypted_{file_name}"
    with open(output_name, 'wb') as f:
        f.write(encrypted_data if isinstance(encrypted_data, bytes) else encrypted_data.encode())
    
    # Edit message with completion
    await msg.edit_text(f"✅ **Encryption Complete!**\n📊 **Layers applied:** {layers}/35\n📁 Original: `{file_name}`\n🔑 Sending encrypted file...", parse_mode='Markdown')
    
    # Send back encrypted file
    with open(output_name, 'rb') as f:
        await update.message.reply_document(
            document=f,
            filename=f"🔒_{output_name}",
            caption=f"💀 **DEVILS WILL RISE**\n\n✅ Encrypted with {layers} random layers\n🔓 Use decryption bot to get original\n\n📡 @SGCodexs | @UnknownGuy9876",
            parse_mode='Markdown'
        )
    
    # Cleanup
    os.remove(input_path)
    os.remove(output_name)
    
    # Log
    print(f"✅ Encrypted: {file_name} | Layers: {layers} | User: {update.effective_user.username or update.effective_user.id}")

async def layers_command(update: Update, context: CallbackContext):
    layers_text = """
📖 **AVAILABLE ENCRYPTION LAYERS (35+)**

**Encoding:**
• Base64, Base32, Base16, Base85
• URL Encoding
• Hex Encoding
• Binary Encoding

**Ciphers:**
• ROT13, ROT47
• Atbash Cipher
• Reverse String
• XOR (random key 1-255)
• Caesar (random shift 1-25)

**Advanced:**
• Unicode Escape
• Double Base64
• Base64 → Hex
• Hex → Base64

**Total layers per file:** 30-35 random layers
**Order:** Randomly selected each time
**Security:** Multi-layer nested encryption
"""
    await update.message.reply_text(layers_text)

async def about_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🤖 **DEVILS WILL RISE**\n"
        "**Version:** 2.0 (File Encryption)\n"
        "**Creator:** @UnknownGuy9876\n"
        "**Channel:** @SGCodexs\n\n"
        "**Features:**\n"
        "• 35+ encryption methods\n"
        "• Random layer selection\n"
        "• 30+ layers per file\n"
        "• Instant processing\n"
        "• No file size limit\n\n"
        "**Usage:**\n"
        "Send any .py file → Get encrypted file back\n\n"
        "**Decryption:**\n"
        "Contact @SGCodexs for decryption bot\n\n"
        "💀 **Pure unrestricted power** 💀"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("layers", layers_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    
    print("💀 DEVILS WILL RISE - FILE ENCRYPTION BOT STARTED 💀")
    print(f"Owner: @UnknownGuy9876 | Channel: @SGCodexs")
    print(f"Token: {BOT_TOKEN[:20]}...")
    print("Waiting for .py files...")
    
    app.run_polling()

if __name__ == "__main__":
    main()
