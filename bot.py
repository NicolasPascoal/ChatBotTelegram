from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7709876744:AAG_jh6IEuZm5MeRqYPt8raXYUtnrrO4F_0" 

#mensagens
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salve, FURIOSO(A)! 🔥\nBem-vindo ao bot da FURIA! \n\n\nAqui, você vai encontrar as últimas atualizações sobre nossos jogos, novidades da equipe, e tudo o que rola no mundo da FURIA! 🎮🔥\n\n\nJunte-se à FURIA e mostre seu apoio! Vamos juntos rumo à vitória! 🏆\n #GOFURIA")

async def mentality(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("construçao")
async def quemSomos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Somos FURIA!\n\n Uma organização de esports que nasceu do desejo de representar o Brasil no CS e conquistou muito mais que isso: expandimos nossas ligas, disputamos os principais títulos, adotamos novos objetivos e ganhamos um propósito maior. Somos muito mais que o sucesso competitivo \n\n\n Somos um movimento sociocultural.")

#times
async def vlr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥TIME DE VALORANT🔥 \n Pryze\n Khalil\n Heat\n Havoc\n COACH: Peu \n\n\n\n 📅PRÓXIMO JOGO: Nao definido até o momento!")

async def cs2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥TIME DE CS2🔥 \n MOLODOY\n YEKINDAR\n FalleN\n KSCERATO\n yuurih\n COACH: Hepa \n\n\n\n 📅PRÓXIMO JOGO\n FURIA vs NAVI \n Data: 17/06 ")

async def fur(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥⚽TIME DA FURIA FC⚽🔥 \n 🧤GOLEIROS🧤 \n Matheus Ayosa\n Victor Hugo\n\n🛡️DEFENSOR🛡️\n Joao Pelegrini\n\n⚽MEIAS⚽\n Caio Catroca\n Andrey Batata\n Matheus Dedo\nJeffinho(Curinga)\n\n🥅ATACANTES🥅\n Guilherme Monogatti\n Murillo Donato\n Ryan Lima\n Gabriel Pastuch\n Lipão(Curinga)\n Leleti(Curinga)")

async def lol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥TIME DE LEAGUE OF LEGENDS🔥\n Guigo(TopLaner)\nTatu(jungler)\nTutsz(MidLaner)\nAyu(Adcarry)\n Jojo(suport) \n\n\n\n 📅PRÓXIMO JOGO\n FURIA vs LOUD\n Data: 27/04 as 15:00")

async def r6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥TIME DE RAINBOW SIX🔥\n KHEYZE\n JV92\n FELIPOX\n HERDSZ\n NADE\n COACH: IGOORCTG ")

#externos
async def redes (update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥REDES SOCIAIS🔥\n Instagram: @furiagg \n Youtube: youtube.com/FURIAgg\n X: @FURIA\n Tiktok: @furia  ")
async def loja (update:Update, context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text("🔥LOJA DA FURIA🔥\n www.furia.gg")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quemSomos", quemSomos))
    app.add_handler(CommandHandler("vlr", vlr))
    app.add_handler(CommandHandler("cs2", cs2))
    app.add_handler(CommandHandler("fur", fur))
    app.add_handler(CommandHandler("lol", lol))
    app.add_handler(CommandHandler("r6", r6))
    app.add_handler(CommandHandler("loja", loja))
    app.add_handler(CommandHandler("redes",redes))
    app.run_polling()