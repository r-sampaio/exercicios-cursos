const env = require ('../.env')
const Telegraf = require('telegraf')
const bot = new Telegraf(env.token)

bot.start (ctx => {
    if(ctx.update.message.from.id === 129018008) {
        ctx.reply('Ao seu dispor!')
    } else {
        ctx.reply(`Eu nao falo com voce!`)
    }
})

bot.startPolling()