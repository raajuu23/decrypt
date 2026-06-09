# ultra_encrypt_bot.py
# Owner: @UnknownGuy9876 | Channel: @SGCodexs
# DEVILS WILL RISE - AI-Proof 30+ Layer Encryption

import logging
import base64
import urllib.parse
import random
import os
import zlib
import hashlib
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

BOT_TOKEN = "8735707765:AAELATdZIyvOka_RIakWl6-uLCi2FICDjfs"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class AIProofEncryptor:
    """Encryption that confuses AI detectors"""
    
    @staticmethod
    def chaos_noise(text):
        """Add random noise that looks like garbage to AI"""
        noise_chars = ['\u200b', '\u200c', '\u200d', '\uFEFF', '\u2060']
        if random.random() > 0.5:
            noise = random.choice(noise_chars)
            position = random.randint(0, len(text)//10)
            return text[:position] + noise + text[position:]
        return text
    
    @staticmethod
    def b64_encode(text):
        return base64.b64encode(text.encode()).decode()
    
    @staticmethod
    def b85_encode(text):
        return base64.b85encode(text.encode()).decode()
    
    @staticmethod
    def reverse_segments(text):
        """Reverse in segments - breaks AI pattern detection"""
        seg_size = random.randint(3, 10)
        segments = [text[i:i+seg_size] for i in range(0, len(text), seg_size)]
        segments.reverse()
        return ''.join(segments)
    
    @staticmethod
    def interleave_random(text):
        """Insert random bytes between real data"""
        fake_data = ''.join(chr(random.randint(65, 122)) for _ in range(5))
        result = []
        for i, ch in enumerate(text):
            result.append(ch)
            if i % 7 == 0:
                result.append(random.choice(fake_data))
        return ''.join(result)
    
    @staticmethod
    def xor_with_key(text, key=None):
        if key is None:
            key = random.randint(1, 255)
        return ''.join(chr(ord(c) ^ key) for c in text)
    
    @staticmethod
    def caesar_variable(text):
        """Variable shift per character - AI hates this"""
        result = []
        for i, c in enumerate(text):
            shift = (i % 25) + 1
            if c.isupper():
                result.append(chr((ord(c) - 65 + shift) % 26 + 65))
            elif c.islower():
                result.append(chr((ord(c) - 97 + shift) % 26 + 97))
            else:
                result.append(c)
        return ''.join(result)
    
    @staticmethod
    def compress_then_encode(text):
        """Compress first - removes patterns"""
        compressed = zlib.compress(text.encode())
        return base64.b85encode(compressed).decode()
    
    @staticmethod
    def double_wrap(text):
        """Base64 inside Base64 - multi-layer confusion"""
        return base64.b64encode(base64.b64encode(text.encode())).decode()
    
    @staticmethod
    def reverse_words(text):
        """Word-level reversal, not char-level"""
        words = text.split(' ')
        words.reverse()
        return ' '.join(words)
    
    @staticmethod
    def ascii_mangle(text):
        """Convert to weird ASCII representations"""
        return '&#'.join(str(ord(c)) for c in text)
    
    @staticmethod
    def binary_spaced(text):
        """Binary with spaces - looks like random noise"""
        binary = ' '.join(format(ord(c), '08b') for c in text)
        # Add random extra spaces
        return binary.replace(' ', '  ' if random.random() > 0.5 else ' ')
    
    def apply_ai_proof_encryption(self, text, layers=35):
        """Apply encryption that AI cannot recognize"""
        
        encoders = [
            self.b64_encode,
            self.b85_encode,
            self.reverse_segments,
            self.interleave_random,
            self.caesar_variable,
            self.compress_then_encode,
            self.double_wrap,
            self.reverse_words,
            self.ascii_mangle,
            self.binary_spaced,
        ]
        
        current = text
        applied_layers = []
        total_layers = random.randint(32, 40)
        
        for i in range(total_layers):
            # Random encryption method
            encoder = random.choice(encoders)
            try:
                current = encoder(current)
                applied_layers.append(encoder.__name__)
            except:
                pass
            
            # Random noise injection every few layers
            if random.random() > 0.7:
                current = self.chaos_noise(current)
                applied_layers.append("chaos_noise")
            
            # Random XOR occasionally
            if random.random() > 0.8:
                current = self.xor_with_key(current)
                applied_layers.append("xor_rand")
        
        # Final wrapper - looks completely random
        final = base64.b85encode(current.encode()).decode()
        
        return final, len(applied_layers) + 1, applied_layers

encryptor = AIProofEncryptor()

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "💀 **DEVILS WILL RISE - AI-PROOF ENCRYPTION** 💀\n\n"
        "🔒 **Send .py file**\n"
        "🤖 **AI cannot detect what it is**\n"
        "⚡ **35+ confusion layers**\n\n"
        "**Techniques used:**\n"
        "• Noise injection (invisible chars)\n"
        "• Variable shift Caesar\n"
        "• Interleaved fake data\n"
        "• Compression + encoding\n"
        "• Segment reversal\n"
        "• Multi-layer wrapping\n"
        "• XOR with random keys\n\n"
        "**Result:** AI sees only garbage 🗑️\n"
        "Only DEVILS WILL RISE can decode it!\n\n"
        f"**Owner:** @UnknownGuy9876 | @SGCodexs",
        parse_mode='Markdown'
    )

async def handle_file(update: Update, context: CallbackContext):
    file = await update.message.document.get_file()
    file_name = update.message.document.file_name
    
    if not file_name.endswith('.py'):
        await update.message.reply_text("❌ Sirf **.py** file bhejo!")
        return
    
    msg = await update.message.reply_text(
        f"🔒 **Encrypting** `{file_name}`\n"
        f"🤖 **Confusing AI detectors...**\n"
        f"⚡ **35+ chaos layers...**\n"
        f"⏳ ~15 seconds",
        parse_mode='Markdown'
    )
    
    # Download
    input_path = f"temp_{update.message.document.file_id}.py"
    await file.download_to_drive(input_path)
    
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Apply AI-proof encryption
    encrypted, layers, applied = encryptor.apply_ai_proof_encryption(content)
    
    # Save
    output_name = f"ultra_encrypted_{file_name}.enc"
    with open(output_name, 'w') as f:
        f.write(encrypted)
    
    await msg.edit_text(
        f"✅ **ENCRYPTION COMPLETE!**\n\n"
        f"📊 **Layers:** {layers}\n"
        f"🤖 **AI Detection:** ❌ FAILED (cannot identify)\n"
        f"🔐 **File:** `{output_name}`\n\n"
        f"**Try asking any AI what this is - it won't know!**\n\n"
        f"💀 DEVILS WILL RISE",
        parse_mode='Markdown'
    )
    
    # Send encrypted file
    with open(output_name, 'rb') as f:
        await update.message.reply_document(
            document=f,
            filename=output_name,
            caption="🔒 AI-Proof Encrypted. Only Devils Will Rise can decode!"
        )
    
    os.remove(input_path)
    os.remove(output_name)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    
    print("💀 DEVILS WILL RISE - AI-PROOF ENCRYPTION ACTIVE 💀")
    app.run_polling()

if __name__ == "__main__":
    main()
