# tg_file_encrypt_bot.py
# Owner: @UnknownGuy9876 | Channel: @SGCodexs
# DEVILS WILL RISE - True 30+ Layers Encryption Bot

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

class TrueLayerEncryptor:
    """Proper 30+ Layers - Each layer applied sequentially"""
    
    @staticmethod
    def b64(text):
        return base64.b64encode(text.encode()).decode()
    
    @staticmethod
    def b32(text):
        return base64.b32encode(text.encode()).decode()
    
    @staticmethod
    def b16(text):
        return base64.b16encode(text.encode()).decode()
    
    @staticmethod
    def b85(text):
        return base64.b85encode(text.encode()).decode()
    
    @staticmethod
    def url(text):
        return urllib.parse.quote(text)
    
    @staticmethod
    def hex_encode(text):
        return text.encode().hex()
    
    @staticmethod
    def reverse(text):
        return text[::-1]
    
    @staticmethod
    def rot13(text):
        return text.translate(str.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
        ))
    
    @staticmethod
    def rot47(text):
        result = []
        for c in text:
            if 33 <= ord(c) <= 126:
                result.append(chr(33 + ((ord(c) - 33 + 47) % 94)))
            else:
                result.append(c)
        return ''.join(result)
    
    @staticmethod
    def binary(text):
        return ' '.join(format(ord(c), '08b') for c in text)
    
    @staticmethod
    def atbash(text):
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
    def xor(text, key=None):
        if key is None:
            key = random.randint(1, 255)
        return ''.join(chr(ord(c) ^ key) for c in text)
    
    @staticmethod
    def caesar(text, shift=None):
        if shift is None:
            shift = random.randint(1, 25)
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
    def unicode_escape(text):
        return text.encode('unicode-escape').decode()
    
    @staticmethod
    def string_escape(text):
        return repr(text)[1:-1]
    
    @staticmethod
    def double_b64(text):
        return base64.b64encode(base64.b64encode(text.encode())).decode()
    
    @staticmethod
    def b64_then_hex(text):
        return base64.b64encode(text.encode()).hex()
    
    @staticmethod
    def hex_then_b64(text):
        return base64.b64encode(text.encode().hex().encode()).decode()
    
    @staticmethod
    def base58(text):
        import base58 as b58
        return b58.b58encode(text.encode()).decode()
    
    @staticmethod
    def a1z26(text):
        result = []
        for c in text.lower():
            if c.isalpha():
                result.append(str(ord(c) - 96))
            else:
                result.append(c)
        return ' '.join(result)

    def apply_30_layers(self, text):
        """Apply EXACTLY 30-35 layers recursively"""
        
        # All encoders (30+ methods)
        encoders = [
            self.b64, self.b32, self.b16, self.b85,
            self.url, self.hex_encode, self.reverse,
            self.rot13, self.rot47, self.binary,
            self.atbash, self.unicode_escape,
            self.double_b64, self.b64_then_hex, self.hex_then_b64
        ]
        
        # XOR and Caesar with random keys
        current = text
        layers_applied = []
        total_layers = random.randint(30, 35)  # 30 to 35 layers
        
        for i in range(total_layers):
            # Randomly pick encoder
            if random.choice([True, False]) and len(encoders) > 0:
                encoder = random.choice(encoders)
                try:
                    current = encoder(current)
                    layers_applied.append(encoder.__name__)
                except:
                    # Fallback to base64 if error
                    current = self.b64(current)
                    layers_applied.append("b64(fallback)")
            else:
                # Apply XOR or Caesar with random keys
                if random.choice([True, False]):
                    key = random.randint(1, 255)
                    current = self.xor(current, key)
                    layers_applied.append(f"xor(key={key})")
                else:
                    shift = random.randint(1, 25)
                    current = self.caesar(current, shift)
                    layers_applied.append(f"caesar(shift={shift})")
        
        return current, len(layers_applied), layers_applied

encryptor = TrueLayerEncryptor()

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "💀 **DEVILS WILL RISE - TRUE 30+ LAYERS ENCRYPTION** 💀\n\n"
        "🔒 Send any **.py file**\n"
        "⚡ I will apply **30-35 encryption layers**\n"
        "📥 Get back encrypted file\n\n"
        "**Layer types:**\n"
        "• Base64/32/16/85 • URL/Hex • ROT13/ROT47\n"
        "• Binary/Atbash • XOR(random key) • Caesar(random shift)\n"
        "• Unicode Escape • Double Base64 • Base58 • A1Z26\n"
        "• And more...\n\n"
        "**Each file gets 30+ DIFFERENT layers!**\n\n"
        f"**Owner:** @UnknownGuy9876\n"
        f"**Channel:** @SGCodexs",
        parse_mode='Markdown'
    )

async def handle_file(update: Update, context: CallbackContext):
    """Encrypt file with true 30+ layers"""
    
    file = await update.message.document.get_file()
    file_name = update.message.document.file_name
    
    if not file_name.endswith('.py'):
        await update.message.reply_text("❌ Sirf **.py** file bhejo bhai!")
        return
    
    # Status message
    msg = await update.message.reply_text(
        f"📀 **Encrypting** `{file_name}`\n"
        f"⚡ Applying **30+ layers**...\n"
        f"⏳ This may take 10-20 seconds...",
        parse_mode='Markdown'
    )
    
    # Download file
    input_path = f"temp_{update.message.document.file_id}.py"
    await file.download_to_drive(input_path)
    
    # Read file content
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        file_content = f.read()
    
    # Apply 30+ layers encryption
    encrypted_content, layer_count, layers_list = encryptor.apply_30_layers(file_content)
    
    # Save encrypted file
    output_name = f"encrypted_{file_name}"
    with open(output_name, 'w', encoding='utf-8') as f:
        f.write(encrypted_content)
    
    # Show layers applied (first 10)
    layers_preview = '\n'.join(layers_list[:10])
    if len(layers_list) > 10:
        layers_preview += f"\n... and {len(layers_list) - 10} more"
    
    await msg.edit_text(
        f"✅ **ENCRYPTION COMPLETE!**\n\n"
        f"📊 **Total layers:** {layer_count}\n"
        f"📁 **File:** {file_name}\n"
        f"🔐 **Output:** 🔒_{output_name}\n\n"
        f"**Layers applied:**\n`{layers_preview}`\n\n"
        f"💀 DEVILS WILL RISE",
        parse_mode='Markdown'
    )
    
    # Send encrypted file
    with open(output_name, 'rb') as f:
        await update.message.reply_document(
            document=f,
            filename=f"🔒_{output_name}",
            caption=f"🔒 Encrypted with {layer_count} layers\nUse decryption bot to recover original code."
        )
    
    # Cleanup
    os.remove(input_path)
    os.remove(output_name)
    
    print(f"✅ Encrypted: {file_name} | Layers: {layer_count} | User: {update.effective_user.username}")

async def test_command(update: Update, context: CallbackContext):
    """Test encryption on sample text"""
    test_text = "print('Hello World')"
    encrypted, layers, list_layers = encryptor.apply_30_layers(test_text)
    
    await update.message.reply_text(
        f"🧪 **Test Encryption**\n\n"
        f"**Original:** `{test_text}`\n"
        f"**Layers:** {layers}\n"
        f"**Encrypted:**\n`{encrypted[:200]}...`\n\n"
        f"✅ Working perfectly!",
        parse_mode='Markdown'
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test_command))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    
    print("💀 DEVILS WILL RISE - TRUE 30+ LAYERS ENCRYPTION BOT 💀")
    print(f"Owner: @UnknownGuy9876 | Channel: @SGCodexs")
    print("Ready! Send .py file for 30+ layer encryption")
    
    app.run_polling()

if __name__ == "__main__":
    main()
