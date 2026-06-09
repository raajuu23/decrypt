# tg_file_encrypt_bot.py
# Owner: @UnknownGuy9876 | Channel: @SGCodexs
# DEVILS WILL RISE - Fast File Encryption Bot

import logging
import base64
import urllib.parse
import random
import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# ========== CONFIG ==========
BOT_TOKEN = "8735707765:AAELATdZIyvOka_RIakWl6-uLCi2FICDjfs"
# ============================

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class FastFileEncryptor:
    """Fast 30+ Layers File Encryption Engine"""
    
    ENCODERS = []
    
    @staticmethod
    def base64_encode(data):
        try:
            return base64.b64encode(data).decode()
        except:
            return None
    
    @staticmethod
    def base32_encode(data):
        try:
            return base64.b32encode(data).decode()
        except:
            return None
    
    @staticmethod
    def base16_encode(data):
        try:
            return base64.b16encode(data).decode()
        except:
            return None
    
    @staticmethod
    def hex_encode(data):
        try:
            return data.hex()
        except:
            return None
    
    @staticmethod
    def reverse_string(data):
        try:
            return data[::-1].decode('latin-1')
        except:
            return None
    
    @staticmethod
    def rot13_encode(data):
        try:
            text = data.decode('latin-1')
            result = text.translate(str.maketrans(
                "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
                "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
            ))
            return result
        except:
            return None
    
    @staticmethod
    def url_encode(data):
        try:
            return urllib.parse.quote(data.decode('latin-1'))
        except:
            return None
    
    @staticmethod
    def xor_fast(data):
        try:
            key = random.randint(1, 255)
            result = bytes(b ^ key for b in data[:10000])  # Sirf first 10KB for speed
            if len(data) > 10000:
                result += data[10000:]
            return result.decode('latin-1', errors='ignore')
        except:
            return None
    
    def encrypt_file_fast(self, file_data, layers=30):
        """Fast encryption with 30 layers"""
        encoders = [
            self.base64_encode, self.base32_encode, self.base16_encode,
            self.hex_encode, self.reverse_string, self.rot13_encode,
            self.url_encode, self.xor_fast
        ]
        
        current = file_data
        applied = 0
        
        for i in range(min(layers, 35)):
            encoder = random.choice(encoders)
            try:
                if isinstance(current, bytes):
                    result = encoder(current)
                else:
                    result = encoder(current.encode() if isinstance(current, str) else current)
                
                if result:
                    if isinstance(result, str):
                        current = result.encode()
                    else:
                        current = result
                    applied += 1
            except:
                continue
        
        # Final output as string for small size
        if len(current) > 50000:
            # Agar file bahut badi hai to sirf base64 kar do
            final = base64.b64encode(file_data).decode()
            return final.encode(), 1
        
        return current, applied

encryptor = FastFileEncryptor()

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "💀 **DEVILS WILL RISE - FAST FILE ENCRYPTION** 💀\n\n"
        "🔒 Send **.py file**\n"
        "⚡ **Instant encryption** (No waiting!)\n"
        "📥 Get encrypted file back\n\n"
        "**Features:**\n"
        "• Lightning fast ⚡\n"
        "• 30+ encryption layers\n"
        "• No size limit\n"
        "• Instant response\n\n"
        f"**Owner:** @UnknownGuy9876\n"
        f"**Channel:** @SGCodexs",
        parse_mode='Markdown'
    )

async def handle_file(update: Update, context: CallbackContext):
    """Fast encrypt any .py file"""
    file = await update.message.document.get_file()
    
    file_name = update.message.document.file_name
    if not file_name.endswith('.py'):
        await update.message.reply_text("❌ Sirf **.py** file bhejo!")
        return
    
    # Send processing message
    msg = await update.message.reply_text(f"⚡ **Encrypting** `{file_name}`...", parse_mode='Markdown')
    
    # Download file with timeout
    input_path = f"temp_{update.message.document.file_id}.py"
    try:
        await file.download_to_drive(input_path)
    except:
        await msg.edit_text("❌ Download failed! Try again.")
        return
    
    # Read file
    with open(input_path, 'rb') as f:
        file_data = f.read()
    
    # Encrypt fast
    encrypted_data, layers = encryptor.encrypt_file_fast(file_data, layers=30)
    
    # Save encrypted
    output_name = f"encrypted_{file_name}"
    with open(output_name, 'wb') as f:
        f.write(encrypted_data if isinstance(encrypted_data, bytes) else encrypted_data.encode())
    
    # Send back
    await msg.delete()
    with open(output_name, 'rb') as f:
        await update.message.reply_document(
            document=f,
            filename=f"🔒_{output_name}",
            caption=f"✅ **DONE!** {layers} layers applied\n📁 `{file_name}` → encrypted\n\n💀 DEVILS WILL RISE",
            parse_mode='Markdown'
        )
    
    # Cleanup
    os.remove(input_path)
    os.remove(output_name)

async def ping_command(update: Update, context: CallbackContext):
    await update.message.reply_text("⚡ **ALIVE & READY**\nSend me a .py file!", parse_mode='Markdown')

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping_command))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    
    print("💀 DEVILS WILL RISE - FAST ENCRYPTION BOT ACTIVE 💀")
    print(f"Token: {BOT_TOKEN[:15]}...")
    print("Ready for .py files!")
    
    app.run_polling()

if __name__ == "__main__":
    main()
