# 🌡️ Projeto de Monitoramento de Temperatura para Secadoras Industriais 🌪️

O que é isso? 🤔
Essa é a aplicação dos sonhos para quem quer evitar que suas secadoras industriais passem do limite! 🚨

Imagina só: uma secadora com sensores IoT que monitoram a temperatura em tempo real, mandam os dados para a nuvem, e ainda te avisam no Telegram se a temperatura estiver prestes a queimar tudo! Isso mesmo, aqui a gente joga seguro para evitar surpresas (e roupas queimadas!).

Por que isso é importante? 💡
Secadoras industriais são maravilhosas para grandes volumes de roupa, mas, se esquentam demais... 💥 os prejuízos podem ser grandes! Queimaduras em tecidos e até danos ao equipamento. E não queremos isso, certo?

Esse projeto foi desenvolvido justamente para manutenção preditiva, garantindo que você saiba exatamente quando as coisas estão esquentando mais do que deveriam e tomar providências antes que os problemas aconteçam.

###  Funcionalidades 🔥
Monitoramento em tempo real das temperaturas de uma secadora industrial.
Alertas automáticos no Telegram quando a temperatura passar de um certo limite (olha o alerta de 94°C aí!).
Histórico de temperaturas disponível via interface web, para você visualizar e analisar as variações.
Integração com Firebase para armazenamento e análise de dados.
MQTT para comunicação rápida e eficiente dos dados dos sensores.

### Tecnologias Usadas 💻
Python 🐍: O cérebro da operação, controlando o backend.

Flask 🌐: Framework web para a interface e o painel de monitoramento.

MQTT 📡: Para a comunicação dos dados entre o sensor e o servidor.

Firebase 🔥: Para armazenar os dados e garantir que você nunca perca um registro de temperatura.

Telegram Bot API 🤖: Porque receber mensagens de alerta no Telegram é muito mais prático do que ter que ficar de olho no termômetro o dia todo!

Plotly 📊: Para criar gráficos interativos e bonitos no painel de histórico.

###  Como isso tudo funciona? 🚀
Monitoramento: A secadora está equipada com sensores que capturam a temperatura ambiente e mandam esses dados para o servidor via MQTT.
Alerta: Quando a temperatura passa dos 94°C, o servidor envia uma mensagem automática para o Telegram com um alerta urgente.
Histórico: Toda a coleta de dados é armazenada no Firebase e pode ser acessada a qualquer momento pelo painel web. Você pode ver todos os registros e analisar os dados para melhorar a operação.

##  LOGIN
![Captura de tela 2024-09-19 192501](https://github.com/user-attachments/assets/ab71fdec-45c0-4c46-805e-7a0d4ccfca61)
##  DASHBOARD 
![Captura de tela 2024-09-19 192702](https://github.com/user-attachments/assets/84150609-2196-430c-b4d4-3871188417b3)
##  HISTORICO
![Captura de tela 2024-09-19 192716](https://github.com/user-attachments/assets/79df79ca-d67c-4d2b-b8cc-1d5ef0b5292f)
##  INSIGHTS
![Captura de tela 2024-09-19 192853](https://github.com/user-attachments/assets/2dd6b6f6-eac6-4002-bba5-0003ee1a4a86)

## TELEGRAM
![WhatsApp Image 2024-09-19 at 19 32 49](https://github.com/user-attachments/assets/ce73bbe0-0b52-465a-bd5f-2f9921363865)



###  Conclusão 🎉
Esse projeto foi criado com o objetivo de aplicar conhecimento teórico na prática e resolver um problema real. Espero que você curta explorar e utilizar essa aplicação tanto quanto eu curti desenvolvê-la!
Se você se preocupava com roupas queimadas na secadora, agora pode ficar tranquilo! 😎
