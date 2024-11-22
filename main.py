import tkinter
import random
from tkinter import messagebox


class app_a_ou_v(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.titre = "Action ou vérité"
        self.taille = "720x480"
        self.fond = "#1C1919"
        self.text = tkinter.Text(self, font=("Cascadia Code SemiBold", 12), bg='#1C1919', fg="white", width=75, height=2)
        self.lst_choix = ["Hot", "Classique", "Soirée", "Sérieux"]
        self.checkbox_vars = []
        self.text = tkinter.Text(self, font=("Cascadia Code SemiBold", 12), bg='#1C1919', fg="white", width=75, height=2)
        
        self.lst_choix = ["Hot", "Classique", "Soirée", "Sérieux"]
        self.checkbox_vars = []
        
        self.a_serieux = [
               "Choisis une personne et dis-lui ce que tu aimes le plus chez elle.",
               "Chosis 2 personnes. Elles devront se dire ce qu'elles aiment le plus et le moins chez l'autre.",
               "Dis-nous quelque chose que tu regrettes et pourquoi tu regrettes.",
               "Dis la première chose que tu me dirais si je perdais la mémoire",
               "Dis la première chose que tu voudrais entendre si tu perdais la mémoire",
               ]
        
        self.v_serieux = [
               "Si un ami te pointait une arme sur le visage, qui serait cet ami et que lui dirais-tu ?",    
               "Tu penses que qui a le plus grand secret parmis les personnes présentes ?",
               "Tu penses que quelle personne souffre le plus au fond ?",
               "Qui voudrais-tu pour te soutenir au quotidien parmis les gens ici ?",
               "Parmis les membres de la secte, qui aurait les pensées les plus sombres selon toi ?",
               "Si tu tombais en dépression, tu penses que quel membre te ferait aller mieux ?",
               "Quel a été le jour le plus triste de ta vie jusqu'à maintenant ?",
               "Quel a été le jour où tu as été le plus heureux jusqu'à maintenant ?",
               "Quelle citation t'inspure le plus au quotidien ?",
               "Selon toi, quelle serait la pire chose qu'on pourrait te faire ?",
               "Quelle fréquentation tu regrettes le plus ?",
               "Quel-est le choix de ta vie qui t'as fait le plus de bien ?",
               "Qu'est-ce qui te donne encore la force de te réveiller ?",
               "Si tu pouvais dire ce que tu veux à qui tu veux, tu dirais quoi et à qui ?",
               "Si tu pouvais recommencer ta vie AVEC tes souvenirs actuels, tu le ferais ? Pourquoi ?",
               "Si tu pouvais recommencer ta vie SANS tes souvenirs actuels, tu le ferais ? Pourquoi ?",
               "Si tu pouvais changer n'importe quoi dans ta vie, tu changerais quoi ?",
               "De quoi as-tu besoin là, maintenant ?",
               "Que penses-tu sincèrement de la Secte ?",
               "Si tu savais que demain tu allais mourir, qu'est-ce que tu ferais ?",
               "Si tu apprenais que demain c'était la fin du monde, qu'est-ce que tu ferais ?",
               "Quelle est la chose la plus gentille que quelqu'un t'ait déjà dit ?",
               "Est-ce que tu penses que de rencontrer ce groupe a changé ta vie ou t'a influencé dans certains choix ?",
               "Quel conseil tu aurais aimé recevoir de quelqu'un ?",
               "Quel-est le problème le plus grave auquel tu ais été confronté ?",
               "Selon toi, quel serait le dilemme le plus horrible auquel répondre ?",
               "Selon toi, quelle serait la chose la plus cruelle que quelqu'un pourrait te faire ?",
               "Quel est ton plus grand regret ?",
               "Si tu apprenais quelque chose sur toi que tu ne savais pas, comment réagirais-tu ?",
               "Si tu tombais en dépression qui serait le mieux placé pour te réconforter ici ?",
               "Quelle question hot tu as toujours voulu me poser ?",
               "Combien d'argent il faudrait te donner pour qu'on ait des rapports ensemble ?",
               ]
        
        self.a_hot = [
            "Mets un objet que je choisis dans tes sous-vêtements",
             "Mets une vidéo porno avec le son à fond pendant 2 minutes",
             "Fais un strip-tease avec ta caméra allumée",
             "Crée une nouvelle position sexuelle et donne-lui un nom",
             "Envoie un sexto à la personne que je vais choisir",
             "Imite ta position sexuelle préférée",
             "Gémis pendant 15 secondes sans rigoler",
             "Envoie un message vocal à une personne de mon choix",
             "Montre la dernière vidéo porno que tu as regardé",
             "Supplie un joueur de te mettre une grosse fessée",
             "Twerk pendant 10 secondes",
             "Cherche ton sextoy de rêve sur internet et montre le aux autres",
             "Improvise une scène d'amour entre toi et une autre personne",
             "Appelle un.e ami.e et demande-lui la taille de son soutien-gorge ou de son pénis",
             "Demande à 2 de tes amis si ils veulent faire un plan à 3 avec toi",
             "Montre un de tes sous-vêtements à la caméra",
             "Fais un Ahegao",
             "Demande à quelqu'un une banane d'une manière très sensuelle",
             "Raconte une blague sexuelle",
             "Embrasse très fortement quelque chose chez toi pendant 20 secondes",
             "Utilise un filtre qui modifie la voix pour dire '' J'ai besoin d'un gros câlin'' de manière très sensuelle",
             "Mime un orgasme (voix + image)",
             "Dis à quelqu'un qu'il a été très vilain",
             "Invente un court poème pour déclarer ton amour à quelqu'un que je choisis",
             "Suce ton doigt de façon érotique",
             "Montre comment tu t'y prendrais pour exciter quelqu'un afin de faire l'amour avec",
             "Drague le joueur de mon choix",
             "Dis ''Dady'' de manière très sexy",
             "Crie le nom de quelqu'un ici présent comme si il te baisait",
             "Prends une vérité.",
             "Si tu as un sextoy, montre le",
             "Fais un classement des personnes de la plus à la moins sexy",
             "Donne un coup de rein à un oreiller",
             "Tu dois imiter quelqu'un qui suce",
             "Prends une photo de toi comme si tu te faisais défoncer",
             "Gémis en disant le nom de quelqu'un du groupe",
             "Enlève un vêtement (hors les chaussettes)",
             "Comporte toi comme si tu avais la dalle (version +18) pendant 5 minutes",
             "Montre du doigt la partie ou t'es le plus sensible",
             "Pendant 3 tours, tu dois choisir une personne dont tu dirais le nom de manière douteuse",
             "Caresse ta jambe sensuellement",
             "Décrire un pénis ou un vagin à voix haute comme si tu faisais cours à des enfants",
             "Mets un coup de rein à un oreiller",
             "Change ton pseudo en ''un truc bien sale''",
             "On va devoir choisir quelqu'un ici, et à chaque fois que tu l'appelleras, tu devras lui donner un nom qu'on choisira aussi.",
             ]
        
        self.v_hot = [
            "Quelle est ta plus grande peur pendant l'acte ?",
            "Est-ce que tu paierais pour avoir des relations sexuelles ?",
            "Quelle est le chose la plus surprenante qui t'a excité ?",
            "Quel fantasme tu ne voudrais jamais essayer dans la vie ?",
            "Tu te verrais bienêtre nudiste ?",
            "Quel a été ton dernier fantasme pendant que tu te masturbais ?",
            "Tu voudrais essayer le BDSM ?",
            "Tu voudrais essayer d'être attaché / d'attacher quelqu'un ?",
            "As-tu déjà fait un rêve érotique de quelqu'un que tu connais ?",
            "Quelle catégorie sur les sites pour adultes tu consutles le plus ?",
            "Si on faisait un strip-poker entre les gens de ce groupe, tu accepterais ?",
            "Si on faisait une orgie que entre les gens de ce groupe, tu accepterais ?",
            "Quelle est la dernière personne sur qui tu as fantasmé ?",
            "Est-ce que tu t'es déjà imaginé faire l'amour avec quelqu'un du même sexe que toi ?",
            "Est-ce que tu aimeras faire l'amour avec quelqu'un du même sexe que toi ?",
            "Qu'est-ce que tu aimerais expérimenter durant les préliminaires ?",
            "Quel est ton secret le plus coquin ?",
            "Si tu devais jouer dans un film porno, quel serait le nom parfait comme titre ?",
             "Plutôt la moitié haut ou la moitié bas ?",
             "Si tu devais jouer dans un film porno, tu jouerais dans quelle catégorie ?"
             "Tu préfères par devant ou par derrière ?",
             "As-tu déjà pensé à faire un plan à 3 ?",
             "Quel est le site pour adulte sur lequel tu vas le plus souvent ?",
             "Quel est le titre de la dernière vidéo porno que tu as regardé ?",
             "A quand remonte la dernière fois que tu t'es masturbé ?",
             "A quand remonte la dernière fois que tu es allé sur un site porno ?",
             "Tu préfères quelqu'un qui est poilu, rasé ou semi-rasé ? Et on parle pas au niveau du visage.",
             "Quelle est la taille de ton pénis / de ton soutien-gorge ?",
             "Quelle est ta position sexuelle préférée ?",
             "Selon toi, quel-est l'endroit de rêve pour faire l'amour ?",
             "Est-ce que tu aimerais faire un plan à 3 ? Si oui avec qui ?",
             "Selon-toi, qui est la personne la plus moche de la pièce ?",
             "Est-ce que tu t'es déjà fait surprendre en train de te masturber ?",
             "A quel endroit tu aimerais te faire caresser ?",
             "Tu voudrais essayer un jeu de rôle +18 ? Si oui, quel serait le thème ?",
             "Quel est l'endroit le plus bizarre où tu t'es masturbé ?",
             "Quel est le moment le plus bizarre pour se masturber selon toi ?",
             "As-tu déjà été secrètement amoureux de quelqu'un ici ?",
             "Quel a été ton dernier fantasme ?",
             "Tu trouves le porno excitant ou dégueulasse ?",
             "Quelle est la catégorie de porno que tu aimes le plus ?",
             "Quelle est la catégorie de porno que tu aimes le moins ?",
             "Quelle action de la catégorie tu ne voudrais surtout pas faire ?",
             "Quelle vérité de la catégorie tu ne voudrais surtout pas avouer ?"
             "La dernière fois que tu t'es masturbé, à qui as-tu pensé ?",
             "Tu préfères faire l'amour dans un endroit inconfortable mais discret ou confortable mais tu te feras peut-être prendre ?",
             "Tu préfères subir un rapport anal, oral ou vaginal ?",
             "Tu préfères faire un rapport anal, oral ou vaginal ?",
             "Quel-est ton outil préféré pour te masturber ?",
             "As-tu déjà fait un rêve érotique ? Si oui, raconte-le.",
             "Quelle partie du corps préfères-tu chez les gens du même sexe que toi ?",
             "Quelle partie du corps préfères-tu chez les gens du sexe opposé à toi ?",
             "Est-ce que tu as déjà regretté que quelqu'un fasse partie de ta famille car tu voulais faire quelque chose avec ?",
             "Si tu devais faire un porno avec quelqu'un ici, tu voudrais que ce soit avec qui ?",
             "Plutôt bottom ou top ?",
             "Plutôt pâtissier ou pâtisserie ?",
             "Où voudrais-tu vraiment faire l'amour avec quelqu'un ?",
             "Quel fantasme sexuel aimerais-tu réaliser avec quelqu'un ici sans nommer personne ?",
             "Avec quel célebrité tu aimerais faire l'amour ?",
             "Quelle est la période d'abstinence la plus longue que tu as déjà eue ?",
             "Tu préfères lécher des pieds ou un cul ?",
             "Tu préfères avoir 3cm de bite dans les fesses toute ta vie ou 15cm dès que tu mates une meuf / un mec ?",
             "A quel mec ici présent tu voudrais faire une gorge profonde ?",
             "Qui voudrais-tu masturber et récupérer ses semences ?",
             "Tu préfères te la prendre par devant ou par derrière ?",
             "Est-ce que tu t'es déjà satisfait avec un objet honteux ? Si oui, lequel ?",
             "Selon toi, qui serait le ''meilleur pâtissier'' ici ?",
             "Selon toi, qui serait la ''meilleure pâtisserie'' ici ?", 
             "Si tu pouvais fouetter les fesses que quelqu'un ici, tu le ferais à qui ?",
             "Qui seraient le meilleur partenaire et le meilleur caméraman pour un film porno parmis les personnes ici ?",
             "Qui serait le meilleur maître sexuel pour toi parmis les gens ici ?",
             "Qui serait le meilleur esclave sexuel pour toi parmis les gens ici ?",
             "Parmis les gens ici, avec qui tu voudrais le plus ken ? Et pourquoi ?",
             "Est-ce que tu as déjà eu envie de faire une partouze ? Si oui, avec qui ?",
             "Quel est ton fantasme actuel ?",
             "As-tu déjà eu honte d'un de tes fantasmes ? Si oui lequel ?",
             "As-tu déjà eu honte de fantasmer sur une personne ? Si oui, laquelle et pourquoi ?",
             "Quel est le temps de ton plaisir solo le plus long ?",
             "Quel est le nombre maximum de fois où tu t'es satisfait en 1 journée ?",
             "Si on te donnait 1000000000€ pour faire une gorge profonde à quelqu'un, à qui tu le ferais ? (Tu es obligé de choisir quelqu'un)",
             "Quelle est la dernière chose sur laquelle tu t'es masturbé ? ",
             "Si t'étais une prosituée, tes services couteraient combien ?",
             "Quelle est la chose la moins éthique que tu voudrais essayer ?",
             "Est-ce que une fois tu voudrais te filmer en plein acte ?",
             "Sur quelle catégorie tu vas le plus sur des sites pornos ?",
             "En moyenne, combien de fois par semaine tu te masturbes ?",
             "Comment tu voudrais que quelqu'un t'appelle au lit ?",
             "Quel est ton fantasme de dessin animé le plus sexy ?",
             ]
        
        self.a_classique = [
               "Dis ''Perry the Platypus'' avec la voix du Dr.Doofenshmirtz",
               "Fais un classement du classement d'un potentiel battle royal parmis les membres de la secte",
               "Fais du air-guitar",
               "Ne parle pas pendant 2 tours",
               "Demande à ChatGPT te t'écrire un stand-up sur le sujet que je veux; tu devras ensuite nous le jouer",
               "Fais-nous une imitation de quelqu'un qui veut nous vendre une formation pour ce que tu veux",
               "Sens tes chaussettes",
               "Prends un accent russe pendant 3 tours",
               "Mime 5 objets que les autres doivent deviner.",
               "Imite un serpent sur ton sol",
               "Va voir quelqu'un de ta famille et demande-lui si il reste du PQ",
               "Chante une chanson choisie par le groupe",
               "Les yeux fermés, dessine quelque chose choisi par le groupe",
               "Imite un membre du groupe",
               "Dis ''Wallah'' à chaque fin de phrase pendant 5 tours",
               "Regarde un membre du groupe et dis lui qu'il est ultra bg",
               "Trouve 5 mots qui rimes avec ton prénom",
               "Prends une vérité.",
               "Fais un pierre-feuille-ciseau avec quelqu'un du groupe",
               "Essaie de faire rire une personne du groupe",
               "Cite un surnom pour chaque personne du groupe",
               "Appelle un numéro de ton répertoire et chante une chanson choisie par le groupe",
               "Mime un animal que les autres doivent deviner",
               "Fais une tour avec des objets de ta chambre et prends une photo",
               "Fais une danse choisie par le groupe",
               "Mets-toi un objet très froid dans le dos pendant 30 secondes",
               "Imite un défile de mannequin",
               "Reste allongé sur le sol pendant jusqu'au prochain tour",
               "Appelle un numéro aléatoire et dis ''je viens récupérer mon enfant dans 20 minutes''.",
               "Imite un animal choisi par le groupe",
               "Imite un de tes parents",
               "Imite quelqu'un de connu et fais-nous deviner",
               "Fais-nous un tour de magie que tu connais",
               "Fais le poirier sur ton mur",
               "Fais un dessin sans lever ton crayon et montre-le nous",
               "Chante ton introduction de dessin animé / d'animé préférée",
               "Donne nous un exemple de chose qui pourrait vraiment mais vraiment te mettre en colère",
               "Fais 10 pompes MAINTENANT",
               "Essaye de jongler avec des objets",
               "Lis à voix haute ta dernière recherche internet",
               "Parle en zozotant pendant 5 minutes",
               "Fais une bonne blague",
               "Dessine toi avec ta main non-dominante",
               "Fais 10 pompes",
               "Fais 10 abdos",
               ]
        
        self.v_classique = [
                "Quelle a été ta première impression sur moi quand on s'est rencontré ?",
                "Si tu pouvais revivre une chose de ta vie, ce serait quoi ?"
                "Quelle est la chose la plus gênante qu'il te soit arrivé en publique ?",
                "Tu préfères Vanille ou Chocolat ?",
                "Quelle est la chose la plus romantique qui tu aies déjà fait ?",
                "Quel est ton moyen préféré pour te détendre ?",
                "Si tu pouvais inviter 3 célébrités à dîner, lesquelles tu inviterais ?",
                "Est-ce que tu as une to-do list ? Si oui, qu'y a-t-il dessus ?",
                "Quel est le plus gros défi que tu ais jamais réalisé ?",
                "Quel est le meilleur conseil que tu n'ais jamais reçu ?",
                "Quelle est la phrase qui t'a le plus marqué de toute ta vie ? Si tu en as plusieurs, tu peux en citer une parmi elles",
                "Quelle action de la catégorie tu ne voudrais surtout pas faire ?",
                "Quelle question tu as toujours voulu me poser ?",
                "Quelle pilule tu choisis entre une qui te fait esquiver tous les tirs et une qui ne te fait rater aucun tir ?",
                "Avec quelle personne tu voudrais jouer à ton jeu favoris et pourquoi ?", 
                "Quelle vérité de la catégorie tu ne voudrais surtout pas avouer ?",
                "Tu ferais quoi avec 1 milliard d'euros ?",
                "Parmis les gens ici, tu penses que qui serait le meilleur président ?",  
                "Si tu étais président et que tu pouvais changer 3 choses en France, ce serait quoi ?",
                "Parmis les gens ici, qui serait le meilleur pour jouer dans un film d'horreur ?",
                "Parmis les gens ici, contre qui tu voudrais te battre et à l'aide de qui ? Et pourquoi ?",
                "Si tu devais choisir quelqu'un pour aller à  la guerre, tu choisirais qui ?",
                "Avec qui tu voudrais fonder une famille parmis les gens ici ?",
                "Avec qui tu voudrais faire un braquage de banque parmis les gens ici ?",
                "Parmis les membres de la secte, choisis le meilleur super vilain et le meilleur super héro",
                "En tant que directeur/directrice d'une école. Donne un rôle à chaque membre de la secte (hors prof)",
                "Qui est le meilleur porteur de la couronne de la secte et de Tinderscord ?",
                "Avec qui tu voudrais faire un duel méga stylé tah les animés ?",
                "Qui tu voudrais comme frère / soeur parmis les gens de la secte ?",
                "Si tu te faisais agresser dans la rue, quel serait la meilleure personne pour te défendre parmis les gens ici ?",
                "Si tu gagnais 1 million d'euros, que ferais-tu avec ?",
                "Quelle est ta musique préférée ?",
                "Quelle est ta série préférée ?",
                "Quel est ton dessin animé / animé favoris ?",
                "Si tu devais faire un bisous à quelqu'un du groupe, qui ce serait ?",
                "Où voudrais-tu être au moment où tu lis cette questions ?",
                "As-tu déjà rêvé de jouer dans un groupe de musique ?",
                "Quel est ton style de musique favoris ?",
                "Si tu devais prendre 2 objets pour aller sur une île déserte, quels seraient-ils ?",
                "Si tu pouvais réaliser un de tes rêves, quel serait-il ?",
                "Si tu pouvais devenir invisible, que ferais-tu ?",
                "Quel genre de film ou de publicité tu voudrais tourner ? Et avec qui ?",
                "Quelle est la plus grande rumeur sur un membre du groupe que tu as déjà entendu ?",
                "Quel est ton plus grand rêve ?",
                "Es-tu plutôt du matin ou du soir ?",
                "Quelle est la plus belle chose que tu ais déjà vu ?",
                "Si Jurassic Park était réel, tu irais le visiter ?",
                "Si tu étais le roi d'un pays, quel serait ton premier ordre ?",
                "Tu préfères avoir un frère / une soeur ou un animal de compagnie ? Pourquoi ?",
                "Entre réaliser ton plus grand rêve et connaître l'amour, que choisirais-tu ?",
                "Quelle est la situation où tu te fais le plus chier ?",
                "Si un jour tu avais un enfant, comment tu l'appellerais ?",
                "Comment tu as découvert que le père noël n'existait pas ?",
                "Est-ce que tu es supersitieux ?",
                "Selon toi, quel serait le pire travail que tu pourrais avoir ?",
                "Quel serait ton travail de rêve ?",
                "Quelle est la blague la plus méchant que tu regrettes maintenant ?",
                "Quel objets tu voudrais le plus au monde ?",
                "Quelle langue tu voudrais le plus apprendre ?",
                "Entre connaître toutes les langues du monde et parler aux animaux, tu choisirais quoi ?",
                "Si tu pouvais devenir n'importe qui existe/a existé, tu deviendrais qui ?",
                "Si tu avais une machine à voyager dans le temps, tu voudrais aller à quelle époque ?",
                "Être pas très riche mais avoir de bon amis et l'amour ou être seul et très riche ?",
                "Quelle personne du groupe tu serais prêt à ne pas voir pendant 1 mois entier ? Pourquoi ?",
                "As-tu déjà tenu une de tes résolutions du nouvel an ? Si oui, laquelle ?",
                "Tu préfères changer ton passé ou voir ton futur ?",
                "Si tu gagnais des courses gratuites dans un magasin, tu voudrais que ce soit lequel ?",
                "Entre savoir jouer de tous les instruments et parler aux animaux, tu choisirais quoi ?",
                "Où voudrais-tu absolument aller en vacances ?",
                "Quelle action de la catégorie tu ne voudrais surtout pas faire ?",
                "As-tu déjà menti à un action ou vérité ? Quelles étaient ta question et ta réponse ?",
                "Si tu devais changer de prénom, lequel tu prendrais ?",
                "Plutôt ville ou campagne ?",
                "Quelle est ta plus grande phobie ?",
                "Est-ce qu'il y a quelque chose que tu as toujours voulu essayer ? Si oui, quoi, pourquoi et pourquoi tu ne le fais pas ?",
                "Si tu pouvais faire grandir une partie de ton corps, ce serat quoi ?",
                "De quel sport ou de quelle activité du voudrais être vraiment très bon ?",
                "Tu préfères être très intelligent ou très riche ?",
                "Est-ce que parfois tu chantes sous la douche ? Si oui, tu chantes quoi le plus souvent ?",
                "Si tu devais te marier, ce serait avec qui et où ça se passerait ?",
                "Si tu n'avais plus qu'un seul jour à vivre, que ferais-tu ?",
                "Est-ce qu'il y a quelque chose que tu achètes très souvent ? Si oui quoi et pourquoi ?",
                "Quel superpouvoir tu voudrais absolument avoir ?",
                "Quelle est la recherche internet dont tu as le plus honte ?",
                "Quel-est ton plus grand tue l'amour ?",
                "Quel est le dernier mensonge que tu as raconté ?",
                "Quel a été le moment le plus gênant de ta vie ?",
                "Du groupe, qui serait le plus susceptible de se faire arnaquer sur internet ?",
                "Est-ce que tu as déjà volé ?",
                "Qui est la personne la plus cringe que tu connaisses ?",
                "Quelle est la chose la plus folle que tu aies faite dans ta vie jusqu'à maintenant ?",
                "Est-ce que tu voudrais faire de la chirugie esthétique ? Si oui, pourquoi ?",
                "Quelle responsabilité tu ne voudrais surtout pas avoir ?",
                "A quoi ressemble ton pyjama préféré ?",
                "Quel travail tu ne pourrais jamais faire ?",
                "Si tu devais supprimer une application de ton téléphone, ce serait laquelle ?",
                "Est-ce que tu as déjà pété et accusé quelqu'un d'autre ?",
                "Quelle odeur tu aimes secrètement mais que les autres n'aiment pas ?",
                "Est-ce que tu as déjà saboté un travail ? Si oui, lequel et pourquoi ?",
                "As-tu déjà ignoré un texto ? Si oui lequel et pourquoi ?",
                "Quel est l'objet que tu préfères dans ta chambre ?",
                "Quelle chose tu ne ferais jamais même pour tout l'argent du monde ?",
                "Si tu pouvais écouter une seule chanson pour le reste de ta vie, quelle serait-elle ?",
                "Quel est le pire conseil que tu ais déjà donné à quelqu'un d'autre ?",
                "Quel est le meilleur conseil que tu ais déjà donné à quelqu'un d'autre ?",
                "Quel est le pire conseil que tu ais déjà reçu de quelqu'un d'autre ?",
                "Quand tu étais enfant, quelle était ta plus grande peur ?",
                "Quelle est la chose la plus bizarre que tu as déjà fait ou que tu fais dans ton sommeil ?",
                "Quelle est la chose la plus effrayante qui te soit déjà arrivée ?",
                "Sur quelle application tu perds le plus de temps ?",
                "Que penses-tu du polyamour ?",
                "Est-ce que tu prends beaucoup de photos ? Si oui, quel-est le genre de capture de plus récurrent ?",
                "Est-ce qu'il y a quelque chose que tu fais souvent devant ton miroir ? Si oui, quoi ?",
                "Quelle est la chose que tu ferais si tu savais qu'il n'y avait pas de conséquences ?",
                "Quelle est la pire habitude que tu as ?",
                "Quel-est le membre du groupe qui t'agace le plus ? Pourquoi ?",
                "Est-ce que tu es jaloux de quelqu'un ? Si oui, de qui et pourquoi ?",
                "Quel est le moment le plus embarassant que tu as vécu en public ?",
                "Est-ce que tu as déjà prétendu être quelqu'un d'autre en ligne ?",
                "Tu préfères être responsable de la mort d'un enfant ou de deux adultes ?",
                "Sur une échelle de 1 à 10, sur combien te considères-tu beau ?",
                "Tu préfères sauver un membre du groupe ou 100 inconnus ?",
                "Quel-est le moment le plus inapproprié où tu as ris ?",
                "Qui est ton ami le plus moche ?",
                "Dans 10 ans, tu penses que qui auras le mieux réussi ?",
                "Quelle est la trend qui t'a le plus cringe de ta vie ?",
                "C'est quoi ton dessin animé préféré de quand tu étais enfant ?",
                "Est-ce que tu as déjà mangé quelque chose de bizarre ? Si oui quoi ?",
                "T'as déjà eu un ami imaginaire ?",
                "Si tu pouvais être n'importe quel personnage fictif, qui ce serait ?",
                "C'est quoi ton talent le plus chelou ?",
                "Est-ce que tu as déjà fait un rêve qui t'a marqué ? Si oui, raconte-le nous.",
                "Quelle est la chanson que tu aimes chanter sous la douche ?",
                "Selon toi, quelle est la qualité la plus sexy que les gens devraient posséder ?",
                "Quelle est la chose la plus folle que tu serais prêt à faire par amour ?",
                "Quelle action tu voudrais absolument me voir faire ?",
                "Quelle vérité tu voudrais absolument que je dise ?",
               ]
        
        self.a_soiree = [
                "Essaie de me draguer",
                "Pendant 1 semaine, tu devras apprendre une danse et te filmer en train de la faire.",
                "Improvise un rap sur une personne que je vais choisir.",
                "Fais le poirier contre ton mur pendant 10 secondes",
                "Montre nous ton talent le plus chelou ",
                "Imite une personne du sexe opposé",
                "Fais une description de la tenue la plus sexy que tu possèdes",
                "Envoie un message à ton/ta crush en disant que quelqu'un l'aime secrètement (ntm si tu peux pas)",
                "Envoie un message à tes parents qui demande de te raconter une anecdote de ta jeunesse que tu devras nous partager",
                "Envoie une question de ''Tu-préfères'' à un ami",
                "Envoie la photo la plus gênante que tu as de moi",
                "Demande à ton crush son date idéal ?",
                "Prends une photo que tu sélectionnes au hasard. A part moi, tout le monde doit la reproduire",
                "Envoie la photo de ton grand daron",
                "Envoie une photo de ta grande daronne",
                "Crie ''Je suis trop un baka UwU''",
                "Tu dois twerker",
                "Chante l'hymne allemand de manière à ce qu'on entende bien comme il faut",
                "Improvise une danse sur une musique choisie par la groupe",
                "Fais semblant d'être en couple avec la personne de mon choix jusqu'à la fin du jeu",
                "Danse pendant 1 minute la danse de mon choix devant tout le monde",
                "Mets toi une big fessée",
                "Appelle un ami à toi et annonce lui quelque chose de random puis raccroche",
                "Raconte un dossier sur toi que tu n'as jamais partagé",
                "Écris-toi un statut avec tes pieds. Tu devras le garder pendant 3 jours",
                "Danse sur une chanson imposée par le groupe",
                "Prends une vérité.",
                "Fais nous ta pire grimace",
                "Envoie une photo de ton historique",
                "Drague un objet dans ta chambre",
                "Touche ton front avec ton pied",
                "Parle sans t'arrêter pendant 1 minutes (sauf si t'as besoin de respirer mskn)",
                "Fais une déclaration d'amour à quelqu'un du groupe",
                "Envoie un poème d'amour à quelqu'un de mon choix",
                "Embrasse ton oreiller pendant 30 secondes",
                "Envoie le message que je veux à qui tu veux",
                "Appelle un numéro au hasard et essaie de tenir une conversation le plus longtemps possible",
                "Dessiner toi quelque chose sur le visage. Évidemment c'est moi qui vais choisir quoi dessiner",
                "Dis l'heure très fort à chaque changement d'heure jusqu'à la fin du jeu",
                "Explique aux autres comment faire les bébés comme si ils étaient jeunes",
                "Écris une chanson de rap sur le thème de mon choix puis envoie un vocal de toi qui la chante",
                "Enlève le vêtement que tu veux",
                "Dis ''Baise-moi'' après chaque phrase jusqu'à ce que ce soit à nouveau ton tour",
                "Mets-toi dans une position imposée par le groupe et attends que quelqu'un la prenne en photo",
                "Chante du Francky Vincent avec de l'eau dans la bouche",
                "Prends un selfie de toi qui fait une duckface et envoie là",
                "Simule un orgasme vite fait",
                "Raconte une anecdote sur toi",
                "Révèle-nous quelque chose sur toi qu'on ne sait pas ",
                "Si tu as un sextoy, montre le",
                "Raconte une anecdote sur toi (que personne ne connaît de préférence)",
                "Rejoue une scène de film jusqu'à ce que quelqu'un devine laquelle c'est",
                "Lis le dernier message que tu as reçu à voix haute.",
                "Appelle un numéro au hasard et demande lui pourquoi la personne t'appelle.",
                "Raconte un rêve totalement wtf que tu as déjà fait",
                "Envoie la photo la plus drôle de ta galerie.",
                "Envoie la dernière photo de ta galerie.",
                "Montre nous ton talent le plus inutile",
                "Montre nous ton talent le plus utile",
                "Appelle un numéro de ton répertoire et drague la personne",
                "Enlève un vêtement",
                "Tu ne dois pas prononcer ''oui'' ou ''non'' pendant 3 tours, sinon tu as un gage",
                "Raconte une blague",
                "Prends un selfie de toi sous un angle pas du tout avantageux",
                "Envoie une phrase random à quelqu'un",
                "Envoie une partie de ton corps très zoomée et fait la deviner aux autres",
                "Envoie un rizz ultra cringe",
                "Fais-nous une bonne blague",
                "Envoie un vocal un peu flirty à ta crush",
                "Envoie un vocal un peu marrant à ta crush",
                "Traverse ta pièce en poirier",
                "Fais un ''Marry, kiss, kill'' avec les gens ici",
                "Appelle ou envoie un message à un de tes parents et dis lui qu'il est puni.",
                "Montre nous la pire photo que tu as sur ton téléphone",
                "Dessine toi un motif de mon choix sur ton front",
                "Fais un geste de la main qui peut dégoûter les autres",
                "Envoie un message à un ami et dis que tu sais ce qu'il a fait hier soir et qu'il devrait en avoir honte",
                "Appelle un restaurant et raconte une blague à la personne au bout du fil",
                ]
        
        self.v_soiree = [
                "Si tu pouvais retirer 1 chose sur Terre, ce serait quoi ?",
                "Tu te verrais bienêtre nudiste ?",
                "es-tu sensible des tétons ?",
                "Quelle action tu voudrais absolument me voir faire ?",
                "Quelle vérité tu voudrais absolument que je dise ?",
                "Qu'est-ce que tu regardes en premier chez quelqu'un qui te plait ?",
                "Selon toi, quelle est la qualité la plus sexy que les gens devraient posséder ?",
                "Quelle est la recherche la plus gênante que tu as déjà fait ?",
                "Quelle est la chose la plus bizarre que tu as déjà fait quand tu été seul à la maison ?",
                "Quand tu es seul chez toi, qu'est-ce que tu fais le plus souvent ?",
                "Si tu devais avoir un nom de strop-teaseuse, ce serait quoi ?",
                "Quel est le plus gros mensonge que tu as déjà réussi à faire avaler ?",
                "Est-ce que quelqu'un t'as déjà vu à poil sans faire exprès ?",
                "Est-ce que tu as déjà vul quelqu'un nu sans faire exprès ?",      
                "Tu accepterais d'aller chercher une crotte de nez en public et de la manger pour combien d'€ ?",
                "Est-ce que tu m'échangerais pour 1 million d'euros ?",
                "Tu penses à quoi quand tu es aux toilettes ?", 
                "Qui est la personne la plus sexy parmi celles présentes ?",   
                "Quelle est la chose la plus gênante qu'il te soit arrivé en publique ?",
                "Quelle est la chose la plus spontanée que tu ne regrettes pas d'avoir fait ?",
                "Quelle est la célébrité sur laquelle tu fantasmes ?",
                "Si tu pouvais échanger ta vie avec une personne dans le monde, qui ce serait et pourquoi ?",
                "Si tu devais devenir un animal, lequel tu deviendrais ?",
                "Quelle est la chose la plus bizarre que tu ais fait pour attirer l'attention de quelqu'un ?",
                "Si tu pouvais être un personnage fictif pendant 1 jour, qui ce serait et pourquoi ?", 
                "As-tu déjà dansé devant un miroir ?",
                "Est-ce que tu chantes sous la douche ? Si oui quoi ?",
                "Quelle est la chose la plus romantique que tu ais déjà fait pour quelqu'un ?",
                "Si tu ne pouvais toucher qu'une partie de mon corps, laquelle ce serait ?",
                "Quelle est la qualité que tu trouves la plus sexy chez un partenaire ?",
                "Quelle question tu as toujours voulu me poser ?",
                "As-tu déjà remis en question ta sexualité ?",
                "Est-ce que tu t'es déjà vu être avec quelqu'un du même sexe que toi ?",
                "Est-ce que tu as déjà rêvé de quelqu'un ici ?",
                "Est-ce que tu pourrais devenir nudiste ? Pourquoi ?",
                "Est-ce que tu as déjà remis en question ta sexualité ? Donne des détails.",
                "Quelle action de la catégorie tu ne voudrais surtout pas faire ?",
                "Parmis les membres de la secte, avec qui tu penses pouvoir survivre le plus longtemps sur une île déserte ?", 
                "Qui serait le plus susceptible de tuer quelqu'un ? Et pourquoi ?", 
                "Avec qui tu voudrais te déchirer la gueule en soirée ?",
                "Qui seraient : Le meilleur cannibal, le meilleur tueur en série et la meilleur victime parmis les personnes présentes.",
                "Tu penses que qui terminera alcolo en premier ?",
                "Tu penses que qui terminera toxico en premier ?",
                "Si tu devais tuer quelqu'un ici ce serait qui ?",
                "Est-ce que tu as déjà aimé quelqu'un du groupe en secret ?",
                "Est-ce que tu t'es déjà imaginé être du sexe opposé ?",
                "Si tu étais du sexe opposé, quelle serait la première chose que tu ferais ?",
                "Quelle est ta plus grande honte ?",
                "Quel est l'endroit le moins adapté où tu t'es masturbé ?",
                "Quelle chose tu voudrais absolument essayer en étant bourré (pour pas que tu t'en rappelles)",
                "Est-ce que tu m'aurais fait un strip-tease pour rire ?",
                "Quelle vérité de la catégorie tu ne voudrais surtout pas avouer ?"
                "Qu'est-ce que tu voudrais que tes parents ne sachent pas sur toi ?",
                "Que penses-tu des soirées échangistes ? Est-ce que tu voudrais essayer ?",
                "Est-ce que tu voudrais essayer la drogue juste une fois ? Si oui, laquelle et pourquoi ?",
                "Quelle est la demande la plus bizarre que quelqu'un t'as déjà fait ?",
                "Quelle est la demande la plus bizarre que quelqu'un t'ais déjà demandé ?",
                "Si tu faisais tomber un truc que tu aimes bien dans un big caca, tu iras le chercher ?",
                "Est-ce que tu as un sextoy ?",
                "Est-ce que tu as déjà mangé quelque chose de bizarre ? Si oui quoi ?",
                "Quel est le texto le plus bizarre que tu ais envoyé ?",
                "Quel est le plus message le plus bizarre que tu ais reçu ?",
                "Quelle est la chose la plus honteuse que tu ais fait car tu en avais envie ?",
                "Quelle est la chose la plus honteuse que tu ais fait car on t'a forcé ?",
                "Quelle a été ta rencontre avec quelqu'un la plus marrante ?",
                "Pour combien tu serais prêt à coucher avec un.e inconnu.e ?",
                "Pour combien tu serais prêt à coucher avec un membre du groupe ?",
                "Est-ce que tu as déjà été intéressé par la moité d'un.e de tes amis.es ?",
                "Est-ce que tu as déjà vu les parties intîmes d'un de tes parents (jeune ou non)?",
                "Aimerais-tu avoir des préliminaires avec une des personnes du groupe ? Si oui, qui ?",
                "Pendant combien de temps max tu as tenu sans dormir ?",
                "Est-ce que tu t'es déjà satisfait avec un objet honteux ? Si oui, lequel ?",
                "Avec combien de personne dans cette pièce tu serais prêt à avoir une aventure ?",
                "Quel est le plus gros mensonge que tu ais raconté ?",
                "Quelle est la chose la plus illégale que tu as déjà fait ?",
                "Quel est le pire cadeau que tu ais reçu ? Comment tu as réagi et comment ça s'est terminé ?",
                "Quelle chose tu veux absolument faire avant de mourir ?",
                "Si tu devais faire quelque chose avec une personne du groupe, avec qui ce serait ? Pourquoi ?",
                "Quelle est la chose la plus malsaine / immorale à laquelle tu ais pensé ?",
                "Quelle est la période la plus longue pendant laquelle tu ne t'es pas touché ?",
                "Selon toi, est-ce que la taille ça compte vraiment ?",
                "Quelle est la chose que tu fait et dont tu as le plus honte ?",
                "Quel-est ton pire red-flag ?",
                "De quelle célebrité tu es secrètement amoureux ?",
                "Quelle est la chose que tu as déjà fait mais que tu jugerais si ça avait été fait par quelqu'un d'autre ?",
                "Si tu pouvais devenir invisible, quelle serait la pire chose à faire selon toi ?",
                "Quand as-tu été indigné pour la dernière fois, pourquoi ?",
                "Si on fouillait dans ta chambre, quelle serait la chose la plus bizarre qu'on pourrait trouver ?",
                "Quelle chose tu fais avec tes amis et que tu ne voudrais pas faire avec ton/ta partenaire ?",
                "Quelle est la chose la plus gênante que tes parents t'aient surpris à faire ?",
                "Quelle est la chose la plus stupide que tu ais déjà fait ?",
                "Qu'est-ce que les gens pensent être vrai à ton sujet, mais en fait ne l'est pas ?",   
                "Qu'est-ce que les gens pensent être faux à ton sujet, mais en fait est vrai ?",
                "Est-ce que tu as déjà raconté une rumeur à propos de quelqu'un ? Si oui, dis-nous la pire que tu ais déjà dite.",
                "Quel est ton souvenir d'enfance le plus embarrassant ?",
                "Quel est le plus grand secret que tu caches à tes parents ?",
                "Si tu te retrouvais en prison, quel serait ton seul appel téléphonique parmis les gens du groupe ?",
                "Quelle est la chose la plus gênante que tu ais déjà partagé avec quelqu'un ?",
                "Est-ce que tu as déjà été surpris en train de faire quelque chose que tu ne devais pas faire ?",
                "Si tu avais la certitude de ne jamais te faire prendre, qui tuerais-tu sur Terre ? ",
                "Hors membre de ta famille, qui tu ne voudrais absolument pas voir nu ?",
                "Quelle est la chose la plus bête que tu ais déjà fait devant un miroir ?",
                "Quelle est la chose que tu pourrais faire mais dont les autres seraient surpris si tu le faisais ?",
                "Quelle photo ou vidéo de toi tu voudrais faire disparaître ?",
                ]
        
        
    def open_tu_pref(self):
        self.destroy()
        self = app_tu_preferes()
        self.tu_pref_things()
        self.tu_pref_root()
        
        
    def get_choice(self):
        lst = [self.lst_choix[i] for i in range(len(self.lst_choix)) if self.checkbox_vars[i].get() == 1]
        return lst


    def action(self):
        lst_actions = []
        
        
        if "Hot" in self.get_choice():
            for i in self.a_hot:
                lst_actions.append(i)
        if "Classique" in self.get_choice():
            for i in self.a_classique:
                lst_actions.append(i)
        if "Soirée" in self.get_choice():
            for i in self.a_soiree:
                lst_actions.append(i)
        if "Sérieux" in self.get_choice():
            for i in self.a_serieux:
                lst_actions.append(i)
            
        if lst_actions ==  []:
            messagebox.showerror("Erreur","Tu dois d'abord choisir une catégorie !")
            return
        
        else:    
            self.text.delete(1.0, tkinter.END)
            self.text.insert(tkinter.END, random.choice(lst_actions))




    def verite(self):
        lst_verites = []
        
        if "Hot" in self.get_choice():
            for i in self.v_hot:
                lst_verites.append(i)
        if "Classique" in self.get_choice():
            for i in self.v_classique:
                lst_verites.append(i)
        if "Soirée" in self.get_choice():
            for i in self.v_soiree:
                lst_verites.append(i)
        if "Sérieux" in self.get_choice():
            for i in self.v_serieux:
                lst_verites.append(i)
                
        if lst_verites == []:
            messagebox.showerror("Erreur", "Tu dois d'abord choisir une catégorie !")
            return

        else:
            self.text.delete(1.0, tkinter.END)
            self.text.insert(tkinter.END, random.choice(lst_verites))
            
            
    def a_ou_v_root(self):
        self.title(self.titre)
        self.minsize(720,480)    
        self.maxsize(720,480)
        self.geometry(self.taille)
        self.config(background=self.fond)
        self.mainloop()
        
    def a_ou_v_things(self):
        title_label = tkinter.Label(self, text="Action ou Vérité ?", font=("Cascadia Code SemiBold", 30), bg='#1C1919', fg="#DE5042")
        title_label.pack()


        self.text.place(x=24, y=150)


        dare_button = tkinter.Button(self, text="Action", font=("Cascadia Code SemiBold", 12), bg="#DE5042", fg="black", command=self.action)
        dare_button.place(x=275, y=250)


        truth_button = tkinter.Button(self, text="Vérité", font=("Cascadia Code SemiBold", 12), bg="#DE5042", fg="black", command=self.verite)
        truth_button.place(x=400, y=250)
        
        for i in range(len(self.lst_choix)):
            var = tkinter.IntVar()
            checkbox = tkinter.Checkbutton(self, text=self.lst_choix[i], variable=var, bg="#1C1919", fg="#DE5042", font=("Cascadia Code SemiBold", 12))
            checkbox.place(x=280, y=300 + 30*i)
            self.checkbox_vars.append(var)


        menu_bar = tkinter.Menu(self)


        file_menu = tkinter.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Tu préfères ?", command=self.open_tu_pref)


        menu_bar.add_cascade(label = "Changer de mode de jeu", menu=file_menu)
        self.config(menu = menu_bar)
        








class app_tu_preferes(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.titre = "Tu préfères"
        self.taille = "720x480"
        self.fond = "#1C1919"
        self.text = tkinter.Text(self, font=("Cascadia Code SemiBold", 12), bg='#1C1919', fg="white", width=75, height=3)
        
        self.lst_choix = ["Hot", "Classique", "Soirée"]
        self.checkbox_vars = []

        
        self.hot = [
            "sucer ton pote ou avoir la calvitie dans 2 ans ?",
            "est-ce que pour sauver la vie de ton pote tu le sucerais ?",
            "mettre ton bras entier dans le cul d'une chèvre ou voir 4 paires de TN devant la chambre de ta future fille ?",
            "toujours être dessus ou toujours être dessous ?",
            "regarder ton partenaire avoir des relations avec un autre ou que ton partenaire te voit avoir des relations avec quelqu'un d'autre ?",
            "avoir des relations sexuelles médiocres quand tu le veux ou avoir une relation sexuelle incroyable 1 fois par mois ?",
            "faire l'amour le matin ou faire l'amour le soir ?",
            "avoir une soirée très romantique ou avoir une soirée très perverse ?",
            "qu'en bas, ton / ta partenaire soit imberbe ou poilu.e ?",
            "faire l'amour sur la plage pendant un couché de soileil ou sur un tapis au coin du feu ?",
            "avoir un orgasme à chaque fois que tu bailles ou avoir un orgasme à chaque fois que tu éternues ?",
            "envoyer un sexto à ton supérieur ou envoyer un sexto à un parent ?",
            "ne faire l'amour que dans une chambre ou faire l'amour partout sauf dans une chambre ?",
            "que tes parents te surprennent en train de faire l'amour ou surprendre tes parents en train de faire l'amour ?",
            "que pendant l'act, tu ais toujours un haut ou que tu ais toujours un bas ?",
            "sortir avec quelqu'un qui kiffe le BDSM ou sortir avec quelqu'un qui est fade pendant l'act ?",
            "regarder quelqu'un faire l'amour ou que quelqu'un te regarde faire l'amour ?",
            "renoncer au porno pendant 1 mois ou renoncer à faire l'act pendant 1 mois ?",
            "faire l'amour avec ton cousin sans que personne ne le sache ou ne pas faire l'amour avec ton cousin mais tout le monde pense que vous l'avez fait ?",
            "faire l'amour dans un lit d'hôtel sale ou dans des toilettes qui puent ?",
            "avoir une bite de 70cm de long ou en avoir une de 7cm ?",
            "avoir une relation sexuelle 2 fois par jours même quand tu ne veux pas ou en avoir 2 fois par mois ?",
            "pouvoir faire l'amour avec la personne la plus sexy du monde ou être en couple avec la personen que tu aimes ?",
            "être en couple avec quelqu'un qui ne te fait jamais l'amour ou avec quelqu'un qui ne te suce jamais ?",
            "faire ta première fois sur le lit de tes parents ou faire ta première fois en dehors d'une chambre ?",
            "vomir à chaque fois que tu as un orgasme ou péter toutes les 3 secondes pendant que tu fais l'amour ?",
            "être une bite ou être un vagin ?",
            "cracher ou avaler ?",
            "donner une recevoir une fessée ?",
            "regarder tes parents dans un film porno ou regarder un film porno avec tes parents ?",
            "faire l'amour ou s'amuser avec nous tous ?",
            "te faire sodomiser tous les samedis soirs par un fan de BDSM ou louer 1 fois ton frère de 4 ans à 3 quincagénaires pédophiles ?",
            "sucer une bite quand tu dis une connerie ou sucer une bite quand tu dis un truc intelligent ?",
            "branler ton pote et personne ne le sait ou ne pas le branler mais tout le monde pense que tu l'as fait ?",
            "participer au gang bang de ta soeur de 18 ans ou prendre sa place ?",
            "voir tes parents faire l'amour dès qu'ils le font ou faire l'amour avec eux une fois et c'est terminé ?",
            "t'asseoir sur une bite et manger un gâteau ou t'asseoir sur un gâteau et manger une bite ?",
            "te taper un membre de ta famille et tout le monde le sait ou te taper tous tes potes et personne ne le sait ?",
            "avoir un orgasme toutes les heures ou avoir un orgasme une fois par mois uniquement ?",
            "te faire sodomiser par une batte de baseball ou te mettre un stylo entier dans l'urètre ?", 
            "coucher avec ton frère / ta soeur ou tuer 3 milliards de personnes ?",
            "te faire sodomiser juste avant de dormir ou te faire sodomiser pour te réveiller ?",
            "enculer ton meilleur ami ou te faire enculer par ton meilleur ami ?",
            "pénétrer une ruche de guêpes ou pénétrer un nid de fourmis rouges ?",
            "avoir un vagin à la place des yeux ou des testicules à la place du nez ?",
            "dire ''couille'' à chaque fois que tu bandes ou dire ''anus'' à chaque fois que tu pètes ?",
            "te faire mettre un cactus de 30cm dans l'anus ou te masturber avec du papier de verre ?",
            "sucer un gode usagé ou branler ton frère / ta soeur ?",
            "perdre ta virginité avec un SDF de 75 ans ou te faire sodomiser par 10 personnes ?",
            "avoir la plus petite bite du monde et baiser un top modèle ou avoir une grosse bite mais ne baiser que des personnes dégueulasses ?",
            "baiser ta moitié avec l'esprit de ta mère à l'intérieur ou baiser ta mère avec l'esprit de ta moitié à l'intérieur ?",
            "te faire dépuceler par un éléphant de 8000kg et baiser toutes les personnes que tu veux ou mourir puceau ?",
            "te faire couper les organes génitaux sans anesthésie ou boire ma chiasse ?",
            "devoir masturber 10000 chameaux ou enculer tous les pigeons que tu vois ?",
            "faire un cuni à une fille qui a ses règles ou faire un cuni à une grand mère de 90 ans ?",
            "avoir une tête de bite, mais une très belle bite ou avoir une tête d'Homme, mais le plus moche des Hommes ?",
            "être scatophile ou être nécrophile ?",
            "être pédophile ou être gérontophile ?",
            "être zoophile ou mourir puceau ?",
            "trouer ton slip dès que tu pètes ou chier dans ton slip dès que tu pètes ?",
            "t'autosucer ou sucer ton père ?",
            "t'autosucer ou te faire sucer par ton père ?",
            "te taper une amie de ta grand-mère et ta famille le sait ou te taper une prof dégueulasse et tout ton lycée le sait ?",
            "que tes parents te voient te toucher ou que ta moitié te voit en train de faire l'amour avec quelqu'un d'autre ?",
            "sucer une bite ou te faire sodomiser ?",
            "avoir une chiasse pendant un date et des toilettes HS ou manger un petit peu de caca tous les matins de ta vie ?",
            "lécher des fesses ou des parties génitales ?",
            "en avoir une grosse et être précosse ou en avoir une petite et être un dieu au lit ?",
            "être épanoui socialement ou être épanoui sexuellement ?",
            "tromper ta moitié ou te faire tromper par ta moitié ?",
            "te faire électrocuter l'organe génital tous les jours de ta vie ou boire 1L de mélange de sperm et de règle 1 fois et c'est terminé ?",
            "ne plus jamais baiser de ta vie ou baiser qui tu veux, mais une fois par semaine tu dois baiser ton père ?",
            "gros seins et petit cul ou gros cul et petits seins ?",
            "sucer Gollum ou te faire sucer par Gollum ?",
            "être une fille et avoir une bite ou être un homme et avoir un vagin ?",
            "sauter dans une piscine de règles ou sauter dans une piscine de sperme ?",
            "un hentai ou un porno ?",
            "faire un porno avec tout ton groupe d'amis ou faire un porno avec tes parents ?",
            "te masturber devant quelqu'un que t'aime ou coucher avec quelqu'un que tu détestes ?",
            "essayer le BDSM ou une nouvelle position sexuelle ?",
            "faire l'amour en public ou dans un avion ?",
            "faire l'amour avec quelqu'un qui a 10 ans de plus que toi ou qui a 10 ans de moins que toi ?",
            "faire l'amour avec une milf ou avec une loli ?",
            "faire l'amour dans le noir ou la lumière allumée ?",
            "être avec quelqu'un qui ne te fait jamais l'amour ou être avec quelqu'un qui ne suce jamais ?",
            "faire l'amour avec une célebrité pas très sexy ou un.e inconnu.e très très sexy ?",
            "faire l'amour avec quelqu'un qui fait BEAUCOUP de bruit ou avec quelqu'un qui reste silencieux ?",
            "faire l'amour avec quelqu'un de beaucoup plus petit que toi ou de beaucoup plus grand que toi ?",
            "explorer le BDSM ou explorer les jeux de rôle ?",
            "être le dominant ou être le dominé ?",
            "être la pâtissier ou être la pâtisserie ?",
            "être avec quelqu'un de poilu ou d'entièrement rasé en bas ?",
            "que pendant l'act, tu doives écouter les gémissements de ta moitié ou écouter des paroles coquines ?",
            "le faire le matin ou le soir ?",
            "le faire avec quelqu'un d'expérimenté ou de débutant ?",
            "que lors des préliminaires, tu puisses utiliser des jouets ou uniquement ton corps ?",
            "le faire dans la douche ou au lit ?",
            "le faire en silence ou avec un fond sonore musical ?",
            "essayer de nouvelles positions ou t'en tenir aux classiques ?",
            "être avec quelqu'un de plus âgé que toi ou de plus jeune que toi ?",
            "avoir un massage ou un strip-tease avant de passer à l'act ?",
            "le faire dans un jacuzzi ou sous la douche ?",
            "le faire avec quelqu'un de sage ou avec quelqu'un de sauvage ?",
            "le faire dans un lit ou sur le sol ?",
            "être menotté ou avoir les yeux bandés ?",
            "faire un lap dance ou que quelqu'un te fasse un lap dance ?",
            "tu préfères menotter ou bander les yeux de quelqu'un ?",
            "recevoir une fessée ou te faire tirer par les cheveux pendant l'act ?",
            "faire l'act ou une séance de pelotage torride ?",
            "que ton partenaire te déshabille ou déshabiller ton partenaire ?",
            "le faire dans un jacuzzi ou le faire dans une piscine ?",
            "que ton partenaire porte un costume ou rien du tout ?",
            "jouer au strip poker ou au strip bottle-spin ?",
            "jouer le rôle d'un pompier ou jouer le rôle d'un policier ?",
            "faire un trio avec ton partenaire ou rester entre vous deux ?",
            "faire un trio avec un autre homme ou avec une autre femme ?",
            "faire un trio avec une personne que tu connais ou avec un.e inconnu.e ?",
            "sucer quelqu'un que tu connais ou sucer un.e inconnu.e ?",
            "attacher ou te faire attacher par ton partenaire ?",
            "faire l'amour dans une cuisine ou dans le salon ?",
            "essayer une nouvelle position ou utiliser un jouet ?",
            "te toucher devant ton partenaire ou te faire toucher par ton partenaire ?",
            "le faire dans un avion ou sur la plage ?",
            "réaliser ton plus grand fantasme ou son plus grand fantasme ?",
            "aller dans un sexshop avec ton partenaire ou regarder un film porno avec ton partenaire ?",
            "vous acheter mutuellement de la lingerie ou que personne ne soit habillé ?",
            "participer à une orgie ou créer un club sexuel en ligne ?",
            "utiliser de la peinture corporelle ou une huile de massage ?",
            "faire des films pornos ou des films hollywoodiens ?",
        ]
        
        self.classique = [
            "te faire prendre en train de remettre ton slip coincer ou te faire prendre en train de te curer le nez et de manger ce que t'y as trouvé ?",
            "avoir une vie de 1000 ans ou 10 vies de 10 ans ?",
            "toujours dire ce que tu penses ou ne plus jamais pouvoir parler ?",
            "perdre l'odorat ou le goût ?",
            "perdre tout ton argent ou tous tes souvenirs ?",
            "avoir toujours chaud ou avoir toujours froid ?",
            "que tout le monde soit heureux, sauf toi ou que tout le monde soit malheureux sauf toi ?",
            "être connu pour quelque chose de terrible ou être inconnu mais avoir fait quelque chose d'extraordinaire ?",
            "être le meilleur joueur d'une équipe nulle ou le pire joueur d'une super équipe ?",
            "pouvoir faire revenir des gens d'entre les morts ou communiquer avec des fantômes ?",
            "recommencer ta vie à 0 avec tous tes souvenirs mais sans connaître ce groupe ou continuer ta vie comme telle ?",
            "pouvoir parler toutes les langues ou savoir jouer de tous les instruments de musique ?",
            "pouvoir parler toutes les langues ou savoir parler aux animaux ?",
            "toujours avoir chaud ou toujours avoir froid ?",
            "être capable de voler ou être capable de devenir invisible ?",
            "contrôler l'eau ou contrôler le feu ?",
            "être SDF mais manger à ta faim ou avoir un toit sur la tête mais manger que 1 repas par jour ?",
            "la trend du ''Quoi -feur'' ou la trend du ''Quoi -coubeh'' ?",
            "toujours avoir 10 minutes de retard ou toujours avoir 20 minutes d'avance ?",
            "avoir 10 chats ou avoir 10 chiens ?",
            "avoir un mauvais salaire dans un emploi que tu adores ou avoir un bon salaire dans un emploi que tu détestes ?",
            "être coincé dans un téléski ou être coincé dans un ascenseur ?",
            "être capable de lire sur les lèvres ou être capable de parler la langue des signes ?",
            "être enlevé par des extraterrestres ou être possédé par un démon ?",
            "sauver 1000 personnes que tu ne connais pas ou sauver 1 personne du groupe ?",
            "être enfermé dans une pièce totalement sombre ou être enfermé dans une pièce constamment lumineuse ?",
            "mourir de froid ou mourir brûlé ?",
            "toujours dire ce que tu penses à voix haute ou ne plus jamais pouvoir communiquer ?",
            "te doucher 1 fois par semaine ou te cogner le petit orteil contre un meuble tous les jours ?",
            "perdre tous tes souvenirs jusqu'à aujourd'hui ou à chaque nouvelle journée, oublier ce qu'il s'est passé la veille ?",
            "toujours avoir faim ou toujours avoir soif ?",
            "être capable de savoir quand on te ment ou pouvoir entendre toutes les pensées de quelqu'un ?",
            "être comme tout le monde ou être différent ?",
            "avoir un corps de rêve mais un visage affreux ou avoir un corps affreux mais un visage de rêve ?",
            "pouvoir déplacer les objets par la pensée ou pouvoir arrêter le temps ?",
            "voir nue toutes les personnes que tu regardes ou lire dans les pensées de tous ceux qui te regardent ?",
            "être une star qui est moche ou être un random et très beau ?",
            "être pauvre en amour et riche en argent ou être riche en amour et pauvre en argent ?",
            "avoir peu d'amis fidèles ou beaucoup d'amis avec qui tu es juste un peu proche ?",
            "être riche et ne pas avoir d'amis ou être pauvre et avoir des amis ?",
            "manger un piment ou te faire frapper ?",
            "savoir comment tu vas mourir ou savoir quand tu vas mourir ?",
            "fêter noël avec ta famille ou fêter noël avec tes amis ?",
            "que quelqu'un te suive toute ta vie ou faire énormément de bruit à chaque pas ?",
            "partir en week-end en oubliant si tu as fermé la porte de la maison ou partir en week-end en oubliant ton téléphone ?",
            "avoir 100 milliards d'euros ou avoir 3 souhaits ?",
            "être dans un ascenseur avec des gens et péter ou roter en plein repas de famille alors que personne ne parle ?",
            "être sourd ou être aveugle ?",
            "avoir un.e partenaire très beau et très riche mais qui ne te rend pas heureux ou bien avoir un.e partenaire pas très beau et pauvre mais qui te comble de bonheur ?",
            "avoir des jambes en mousse ou avoir des dents en bois ?",
            "avoir des dents qui jouent de la musique quand tu manges ou entendre ''DING'' dès que tu clignes des yeux ?",
            "dire ''oui'' à chaque question qu'on te pose ou que les autres te disent ''oui'' à chaque question que tu poses ?",
            "manger 250g de beurre ou sniffer 15cm de sel ?",
            "avoir une langue de 20cm ou un sourire d'abruti complet ?",
            "avoir les yeux à la place des tétons ou avoir le nez à la place de la bite ?",
            "ne pas avoir d'électricité ou ne pas avoir d'eau ?",
            "mesurer 3m50 ou mesurer 1m ?",
            "t'appeler Thomas Tfarci ou t'appeler Jean Bon ?",
            "vivre dans un monde sans musique ou vivre dans un monde sans télé / vidéos ?",
            "faire un saut à l'élastique de plus de 500m de haut ou être enfermé pendant 1 an dans une prison horrible ?",
            "faire un rêve tellement bien que tu as le seum de t'être réveillé ou faire un horrible cauchemar et être heureux de t'être réveillé ?",
            "perdre au ping pong contre quelqu'un qui joue avec une poêle ou perdre au vélo contre quelqu'un en trotinette ?",
            "avoir un téléphone de 12kg ou avoir un téléphone si petit qu'il te faille une aiguille pour l'utiliser ?",
            "avoir un bras au milieu du ventre ou avoir un doigt au milieu du front ?",
            "être mort et un fantôme ou être vivant mais invisible ?",
            "avoir un monosourcil ou ne plus avoir de sourcils ?",
            "ressembler à un samouraï ou ressembler à un viking ?",
            "te laisser pousser les ongles pendants 1 an ou te laisser pousser les poils pendant 1 an ?",
            "tuer tes parents ou manger un arbre entier ?",
            "''1, 2, 3, PARTEZ'' ou ''3, 2, 1, PARTEZ'' ?",
            "avoir une patate brulante dans la bouche ou avoir les mains et les lèvres qui collent ?",
            "avoir les cheveux roses pétants ou t'habiller mal tous les jours ?",
            "être un homme ou être une femme ?",
            "Mario ou Sonic ?",
            "savoir que Sonic est le 6ème personnage le plus recherché des jeux vidéos sur pornhub en 2023 ou savoir qu'un daltonien peut être épileptique ?",
            "travailler à Paris et vivre en campagne ou travailler à Paris et vivre à Paris ?",
            "l'été ou l'hiver ?",
            "habiter une grande maison mais moche ou habiter une petite maison mais belle ?",
            "avancer dans la lumière mais seul ou avancer dans le noir avec un ami ?",
            "la raclette ou la fondue ?",
            "le sucré ou le salé ?",
            "que quelqu'un te crache sur la figure à un moment aléatoire de la journée ou terminer des les embouteillages dès que tu prends la voiture ?",
            "courir 6km tous les jours et manger ce que tu veux ou ne rien faire de tes journées et ne manger que des soupes et des salades chaque jour ?",
            "tuer ton/ta partenaire ou tuer les gens ici présents ?",
            "manger des pâtes au chocolat ou manger une pomme au ketchup ?",
            "constamment respirer par la bouche ou devoir cligner des yeux toutes les secondes ?",
            "avoir des sourcils de 20cm ou avoir une touffe de poils sur le dos de la main ?",
            "être beau mais bêtes ou être bête mais intelligent ?",
            "te faire manger par un requin ou te faire tuer par une noix de coco qui tombe sur toi ?",
            "passer la nuit dans un manoir avec un orage ou être seul chez soi et entendre des bruits dans la cuisine ?",
            "passer la nuit dans une maison hantée ou passer la nuit dans un hôpital psychatrique abandonné ?",
            "être un dragon ou avoir un dragon ?",
            "tes amis ou ton/ta partenaire ?",
            "ne plus jamais pouvoir prononcer la lettre R ou ajouter la lettre R à chaque mot que tu dis ?",
            "habiter dans une maison de 100 pièces ou habiter dans un appartement de 2 pièces ?",
            "avoir l'accent de Marseille ou avoir l'accent du nord ?",
            "que ton eau soit les eaux usées de tes voisins ou ne pas avoir de toilettes et devoir faire tes besoins dans le jardin ?",
            "que tout le monde t'ignore et que tu t'en rendes compte ou que tout le monde te raconte sa vie même quand tu en as marre ?",
            "être le seul à avoir raison ou être d'accord avec tout le monde mais ils ont tous tords ?",
            "prendre une douche glacée ou prendre une douche bouillante ?",
            "avoir le visage de Brad Pitt ou avoir le cerveau d'Einstein ?",
            "courir 500m pieds nus sur un sol de clou ou faire 10 pompes sur un sol brûlant ?",
            "qu'il fasse tout le temps nuit ou qu'il fasse tout le temps jour ?",
            "ne jamais être en couple avec la personne que t'aimes et la voir heureuse ou être en couple avec la personne que t'aimes mais elle est malheureuse",
            "mourir brûlé ou mourir noyé ?",
            "avoir une haleine de poney ou des pieds qui puent ?",
            "avoir plusieures aventures et terminer seul.e ou en avoir une seule à 40 ans et incroyable ?",
            "rester comme tu es ou devenir millionaire mais avec 20% de chance de mourir tout de suite ?",
            "rajeunir de 10 ans ou vieillir de 10 ans ?",
            "être le premier de tes amis à mourir ou être le dernier de tes amis à mourir ?",
            "être immortel ou mourir dans 10 ans ?",
            "rencontrer tes ancêtres ou ta descendence ?",
            "pouvoir voyager dans le passé ou pouvoir voyager dans le futur ?",
            "câliner un panda ou câliner un koala ?",
            "gagner à la lotterie ou vivre 2 fois plus longtemps ?",
            "être maladroit physiquement ou gênant socialement ?",
            "une vie sans café ou une vie sans chocolat ?",
            "vivre dans un monde sans musique ou dans un monde sans téléphone ?",
            "être immortel ou avoir 9 vies ?",
            "ne jamais pouvoir dire non ou ne jamais pouvoir dire oui ?",
            "avoir toujours faim ou être toujours fatigué ?",
            "que ça te démange h24 ou que tu transpires h24 ?",
            "voler mais à la vitesse où tu marches ou courir à la vitesser d'une voiture ?",
            "toujours avoir un caillou dans la chaussure ou toujours avoir un cil dans l'oeil ?",
            "avoir une intelligence surnaturelle ou une force surnaturelle ?",
            "explorer l'espace ou explorer les océans ?",
            "te transformer en n'importe quel animal ou en n'importe quelle personne ?",
            "avoir un bouton de rembobinage de ta vie ou un bouton pause de ta vie ?",
            "que les autres sachent ce que tu fais de ta journée ou que les autres sachent ce que tu dis dans la journée ?",
            "pouvoir faire la taille d'une fourmi quand tu veux ou pouvoir faire la taille d'un immeuble de 2 étages quand tu veux ?",
            "trouver le véritable amour ou trouver une valise de 5 millions d'euros ?",
            "oublier qui tu es ou oublier qui sont les autres ?",
            "pouvoir parler aux animaux ou parler aux morts ?",
            "être fou et le savoir ou être fou mais penser que tu es sain ?",
            "être coincé sur une île déserte seul.e ou avec quelqu'un qui parle sans arrêt ?",
            "être un chien ou être un chat ?",
            "toujours avoir un bout de salade entre les dents ou toujours avoir une coupe de cheveux de merde ?",
            "avoir un monosourcil permanent ou une moustache permanente ?",
            "ne pouvoir que chuchoter ou ne pouvoir que crier ?",
            "perdre tout ton argent ou ne plus jamais pouvoir en gagner ?",
            "ne plus jamais scroller sur les réseaux sociaux ou ne plus jamais regarder de films et de séries ?",
            "passer 1 an seul dans une cabane dans une forêt ou passer 1 an en prison ?",
            "pouvoir voyager dans le temps ou voyager dans l'espace ?",
            "pouvoir voyager dans le temps ou arrêter le tempss ?",
            "perdre ton sens du goût ou ton sens de l'odorat ?",
            "être sans émotions ou être un tsunami d'émotions ?",
            "trouver le grand amour ou le bonheur absolu ?",
            "être respecté ou être aimé ?",
            "être immortel ou avoir une richesses illimitée ?",
            "rammener un proche décédé ou savoir quand et comment tu vas mourir ?",
            "parler aux fantômes ou voyager dans le temps ?",
            "avoir un pouvoir illimité ou une connaissance illimitée ?",
            "pouvoir changer quelque chose en toi ou changer quelque chose dans le monde ?",
            "avoir une cabane dans les arbres ou un trampoline géant dans ton jardin ?",
            "être un détective ou un espion ?",
            "faire un truc chill à la maison ou une soirée de ouf en boîte ?",
            "être avec quelqu'un d'intelligent mais chiant ou de con mais marrant ? (ici on parle de couple)",
            "passer une nuit en camping ou dans un hôtel de luxe ?",
            "regarder un film romantique ou un film d'horreur ?",
            "porter le même look tous les jours ou ne plus jamais pouvoir enfiler un jean ?",
            "avoir un super-pouvoir ou gagner au loto ?",
            "toujours obtenir tout ce que tu veux ou ne plus jamais te prendre la tête ?",
            "avoir une bande de potes ou un meilleur ami ?",
            "pouvoir voler ou vivre sous l'eau ?",
            "partir en croisière ou en vacances exotiques ?",
            "avoir de l'argent illimité ou du temps illimité ?",
            "vivre dans un climat chaud ou vivre dans un climat froid ?",
            "toujours être seul ou n'avoir aucun moment pour toi ?",
            "avoir une longue vie ennuyeuse ou une vie épanouissante ?",
            "recevoir une lettre d'amour ou recevoir un bouquet de fleur ?",
            "un chien qui parle ou un chat qui vole ?",
            "avoir une force surhumaine ou savoir voler ?",
            "ne plus jamais attendre ou ne plus jamais faire la vaisselle ?",
            "savoir jouer de tous les instruments de musique ou savoir être très bon dans tous les sports ?",
            "ne plus jamais avoir besoin de manger ou ne plus jamais avoir besoin de dormir ?",
            "ne plus jamais pouvoir utiliser internet ou ne plus jamais pouvoir sortir de chez toi ?",
            "être le meilleur chanteur du monde ou être le meilleur danseur du monde ?",
            "vivre le reste de ta vie sur une île déserte ou vivre le reste dans une réalité virtuelle ?",
            "être la personne la plus célèbre au monde ou être la personne la plus intelligente au monde ?",
            "être le politicien le plus influent du monde ou être le meilleur athlète du monde ?",
            "ne plus jamais ressentir la douleur physique ou ne plus jamais ressentir la douleur émotionnelle ?",
            "pouvoir contrôler la météo ou contrôler la chance ?",
            "être la personne la plus forte du monde ou la personne la plus intelligente au monde ?",
            "vivre dans une grande ville ou à la campagne ?",
            "être le PDG d'une grande entreprise ou la star d'une émission célèbre ?",
            "renoncer à ton téléphone ou renoncer à ton ordinateur ?",
            "un couple parfait ou une carrière réussie ?",
            "vivre une vie sans but ou une vie sans regrets ?",
            "jouer au tu préfères avec nous ou faire quelque chose de ton côté ?",
            "trouver le grand amour te ta vie mais ne plus jamais nous voir ou ne jamais trouver le grand amour mais tu continues de nous voir ?",
            "être la personne la plus intelligente de la pièce ou la personne la plus drôle de la pièce ?",
            "porter un col-roulé tous les jours de ta vie ou porter une écharpe tous les jours de ta vie ?",
            "être un modo discord ou un modo reddit ?",
        ]

        self.soiree = [
            "te battre contre 10 clones de toi de 10 ans ou te battre contre 1 clone de toi de 30 ans ?",
            "faire des films pornos ou des films hollywoodiens ?",
            "tuer une personne ou la violer ?",
            "est-ce que pour avoir un superpouvoir tu serais prêt à manger que du caca pendant 1 an (genre vraiment que ça) ?",
            "n'avoir plus qu'un seul bras ou n'avoir plus qu'une seule jambe ?",
            "devenir un furry ou devenir nudiste ?",
            "avoir une force surhumaine mais un orgasme dès que tu t'en sers ou ne rien changer à ta vie ?",
            "être obligé de marcher sur les mains ou être obligé de ramper comme un serpent ?",
            "porter des sandales tous les jours de ta vie ou porter un chapeau de cow-boy tous les jours de ta vie ?",
            "aller au travail en rouleurs ou aller au travail en monocycle ?",
            "écouter Nyan Cat dès que tu entres dans une pièce ou écouter Baby Shark dès que tu entres dans une pièce ?",
            "éternuer dès que tu rigoles ou sauter à cloche pied dès que tu te mets en colère ?",
            "danser dès que tu entends de la musique ou chanter dès que tu entends ton nom ?",
            "être obligé de parler comme Yoda ou être obligé de marcher comme un pingouin ?",
            "réciter l'alphabet dès que tu entends ton nom ou ne plus jamais pouvoir dire ''oui'' ?",
            "devoir porter une cape h24 ou ne parler qu'en rimes ?",
            "manger un oignon cru tous les jours ou boire un vers de jus de cornichon tous les jours ?",
            "pouvoir parler avec ton animal de compagnie ou qu'il puisse te répondre ?",
            "porter une cape jusqu'à la fin de ta vie ou porter un costard cravate jusqu'à la fin de ta vie ?",
            "danser pendant 10 minutes à chaque SMS reçu ou danser pendant 10 minutes à chaque mail reçu ?",
            "dire Miaou dès que tu rigoles ou aboyer dès que tu es en colère ?",
            "pouvoir faire tomber les gens amoureux de toi sans possibilité d'inversion ou pouvoir te faire oublier de quelqu'un sans possibilité d'inversion ?",
            "pouvoir faire dire la vérité à n'importe qui ou pouvoir faire gober un mensonge à n'importe qui ?",
            "voler comme un poisson ou nager comme un oiseau ? (oui j'ai fait exprès)",
            "pouvoir te transformer en n'importe quel animal ou te transformer en n'importe quel objet ?",
            "pouvoir arrêter le temps ou pouvoir ralentir le temps ?",
            "pouvoir te clôner ou pouvoir créer des illusions ?",
            "tuer 1 personne de toi-même ou laisser 10 personnes mourir à cause de toi ?",
            "avoir un savoir illimité mais pas pouvoir le transmettre ou avoir un pouvoir sans pouvoir l'utiliser (sauf chez toi) ?",
            "gagner toutes les disputes que tu as ou ne plus jamais devoir te battre ?",
            "devenir le plus grand menteur de tous les temps ou être obligé de dire la vérité ?",
            "pouvoir voler mais ne plus jamais toucher le sol ou savoir respirer sous l'eau mais ne plus jamais remonter à la surface ?",
            "devoir porter un tutu dès que tu vas faire des courses ou chanter à chaque fois que tu es au téléphone (ou en appel discord) ?",
            "pouvoir changer de sexe à volonté ou pouvoir changer d'apparence à volonté ?",
            "contrôler la météo ou contrôler la technologie ?",
            "pouvoir devenir invisible ou pouvoir traverser les murs ?",
            "pouvoir te téléporter n'importe où mais tu te casses la figure à chaque fois ou pouvoir voler mais à 10km/h ?",
            "être un super-héro ou un sorcier ?",
            "pouvoir courir super vite ou pouvoir sauter super haut ?",
            "pouvoir voyager dans le temps, mais ne jamais pouvoir revenir à ton époque ou lire dans les pensées, mais sans que y ait d'interruptions ?",
            "toujours devoir porter un nez de clown ou toujours devoir porter des chaussures de clown ?",
            "avoir un nez énorme ou des oreilles monstrueuses ?",
            "qu'une musique se joue dès que tu rentres dans une pièce ou que des confettis te tombent dessus dès que tu rentres dans une pièce ?",
            "toujours sentir la pizza ou toujours senti l'ail ?",
            "avoir un chat qui parle ou avoir un chien qui parle ?",
            "avoir une licorne en animal de compagnie ou un dragon en animal de compagnie ?",
            "avoir des montagnes russes sans fins ou un toboggan aquatique sans fin ?",
            "boucher tes toilettes à ton travail ou chez ta moitié ?",
            "avoir une peau qui change de couleur selon tes émotions ou avoir des tatouages qui décrivent ce que t'as fait la veille et qui changent chaque jour ?",
            "péter à chaque fois que tu ris ou péter à chaque fois que tu pleures ?",
            "pouvoir parler aux animaux ou parler aux morts ?",
            "avoir constamment le nez qui gratte ou avoir constamment les fesses qui grattent ?",
            "avoir le nez d'un chien ou les yeux d'un chien ?",
            "avoir la voix de Marge Simpson ou les cheveux de Marge Simpson ?",
            "sauter dans une piscine de merde ou sauter dans une piscine de pisse ?",
            "prendre un bain de pisse ou ne pas te laver pendant 2 mois ?",
            "roter entre chaque mot ou dire une insulte monstrueuse à chaque fin de phrase ?",
            "boire 1L de règles ou 1L de sperme ?",
            "être avec quelqu'un que tu aimes, mais pas ouf au lit ou être avec quelqu'un que tu n'aimes pas mais qui est incroyable au lit ?",
            "gros seins et petit cul ou gros cul et petits seins ?",
            "sortir avec ton pote ou sortir avec ton ennemi ?",
            "manger de la merde ou boire de la pisse ?",
            "t'essuyer les fesses avec du papier de verre ou t'essuyer les fesses avec une râpe à fromage ?",
            "voir du gazon sur la tête ou que ta mère ouvre un sexshop ?",
            "un.e partenaire chiant.e mais bg ou pas chiant.e mais moche ?",
            "casser ton téléphone ou te casser une main ?",
            "être un pédophile ou être un terroriste ?",
            "faire l'amour à un zombie ou faire l'amour à un squelette ?",
            "lécher le sol d'une station de métro ou lécher la cuvette d'une toilette publique ?",
            "tuer 1 innocent ou tuer 5 personnes qui ont commis un délit mineur ?",
            "tuer un bébé chat ou être malade le reste de ta vie ?",
            "que chaque personne que tu regardes décède ou que chaque personne que tu regardes te mette un immense coup dans le museau ?",
            "te faire caresser la cuisse par Hitler ou te faire embrasser par Staline ?",
            "être en couple ou être célibataire ?",
            "avoir des saucisses à la place des doigts ou avoir des poêles à la place des pieds ?",
            "vivre le même jour jusqu'à la fin de ta vie ou oublier chaque jour que tu vis ?",
            "passer un jour à la plage avec un string léopard ou passer une journée à la plage avec des brassards Hello Kitty ?",
            "te réveiller sans un oeil ou te réveiller sans une oreilles ?",
            "te faire postillonner à la figure dès que tu parles à quelqu'un ou postillonner dès que tu parles ?",
            "avoir des spaghettis à la place des cheveux ou avoir des cheveux pleins de chewing-gums ?",
            "avoir 4 bras ou avoir 4 jambes ?",
            "devenir noir ou devenir homosexuel ?",
            "être épanoui socialement ou être épanoui sexuellement ?",
            "avoir un bec de canard ou avoir un groin de cochon ?",
            "avoir une jeune prof très sexy (et peut-être avoir ta chance) ou avoir un vieux prof très sympa ?",
            "venir tous les jours en sous-vêtement au collège ou venir un jour tout nu au collège ?",
            "pendant un date, ne pas péter et avoir mal au ventre tout le reste du repas ou péter en espérant que ça ne pue pas ?",
            "être dresseur de pokémon ou être président de la république ?",
            "être à la caisse du supermarché mais ne pas pouvoir payer ou accompagner ton/ta partenaire pendant une journée entière de shopping ?",
            "avoir un cou de girafe ou ne pas avoir de coup du tout ?",
            "être un homme avec une voix de femme ou être une femme avec une voix d'homme ?",
            "vivre seul toute ta vie ou vivre avec un psycopathe toute ta vie ?",
            "sortir avec quelqu'un de moche mais intelligent ou sortir avec quelqu'un de beau mais profondément con ?",
            "chanter la macaréna dans une église ou danser nu.e la macaréna dans la neige à la sortie d'une église ?",
            "être une partie intime ou être des fesses ?",
            "mourir de rire (littéralement) ou mourir juste après avoir fait l'act ?",
            "te laver avec du caca ou te laver avec du vomi ?",
            "avoir des pieds à la place des mains ou avoir des mains à la place des pieds ?",
            "manger 1kg de sable ou boire 1L de crème solaire ?",
            "manger un ongle de pied ou manger une crotte de nez ?",
            "regarder tes parents dans un film porno ou regarder un film porno avec tes parents ?",
            "te faire surprendre par ta moitié en train de coucher avec un de tes amis ou surprendre ta moitié coucher avec un de tes amis ?",
            "perdre la vue ou perdre tes parties génitales ?",
            "avoir des jambes de géant ou des jambes de nain ?",
            "sortir avec quelqu'un qui te snobe ou ne jamais connaître l'amour ?",
            
        ]
        
        
    def open_a_ou_v(self):
        self.destroy()
        self = app_a_ou_v()
        self.a_ou_v_things()
        self.a_ou_v_root()
        
        
    def get_choice(self):
        lst = [self.lst_choix[i] for i in range(len(self.lst_choix)) if self.checkbox_vars[i].get() == 1]
        return lst        
        
        
    def phrase(self):
        
        lst_finale = []
        
        if "Hot" in self.get_choice():
            for i in self.hot:
                lst_finale.append(i)
        if "Classique" in self.get_choice():
            for i in self.classique:
                lst_finale.append(i)
        if "Soirée" in self.get_choice():
            for i in self.soiree:
                lst_finale.append(i)

                
        if lst_finale == []:
            messagebox.showerror("Erreur", "Tu dois d'abord choisir une catégorie !")
            return

        else:
            self.text.delete(1.0, tkinter.END)
            self.text.insert(tkinter.END, "Tu préfères " + random.choice(lst_finale))
        
        
    def tu_pref_root(self):
        self.title(self.titre)
        self.minsize(720,480)    
        self.maxsize(720,480)
        self.geometry(self.taille)
        self.config(background=self.fond)
        self.mainloop()
        

    def tu_pref_things(self):
        title_label = tkinter.Label(self, text="Tu préfères ?", font=("Cascadia Code SemiBold", 30), bg='#1C1919', fg="#DE5042")
        title_label.pack()


        self.text.place(x=24, y=100)


        button = tkinter.Button(self, text="Générer une nouvelle phrase", font=("Cascadia Code SemiBold", 12), bg="#DE5042", fg="black", command=self.phrase)
        button.place(x=240, y=230)


        

        for i in range(len(self.lst_choix)):
            var = tkinter.IntVar()
            checkbox = tkinter.Checkbutton(self, text=self.lst_choix[i], variable=var, bg="#1C1919", fg="#DE5042", font=("Cascadia Code SemiBold", 12))
            checkbox.place(x=280, y=300 + 30*i)
            self.checkbox_vars.append(var)
            
        
        menu_bar = tkinter.Menu(self)


        file_menu = tkinter.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Action ou Vérité ?", command=self.open_a_ou_v)

        menu_bar.add_cascade(label = "Changer de mode de jeu", menu=file_menu)
        self.config(menu = menu_bar)






if __name__ == "__main__":
    window = app_a_ou_v()
    window.a_ou_v_things()
    window.a_ou_v_root()



