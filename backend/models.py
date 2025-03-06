from database import db

# ---------------- EMPLOYE & ENTREPRISE ---------------- #
class EntrepriseCliente(db.Model):
    __tablename__ = 'EntrepriseCliente'
    IDEntreprise = db.Column(db.Integer, primary_key=True)
    nomEntreprise = db.Column(db.String(255), nullable=False)
    statutJuridique = db.Column(db.String(100), nullable=True)

class Employe(db.Model):
    __tablename__ = 'Employe'
    IDEmploye = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    prenom = db.Column(db.String(255), nullable=False)
    numTel = db.Column(db.String(20), nullable=False)
    adresseMail = db.Column(db.String(255), unique=True, nullable=False)
    motDePasse = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    creeParID = db.Column(db.Integer, db.ForeignKey('Employe.IDEmploye', ondelete="SET NULL"), nullable=True)
    dateCreationCompte = db.Column(db.DateTime, nullable=False)
    compteDesactive = db.Column(db.Boolean, default=False)
    mdpModifieLe = db.Column(db.DateTime, nullable=True)
    derniereConnexionLe = db.Column(db.DateTime, nullable=True)
    entrepriseAffiliee = db.Column(db.Integer, db.ForeignKey('EntrepriseCliente.IDEntreprise', ondelete="CASCADE"), nullable=False)

# ---------------- MISSION ---------------- #
class Mission(db.Model):
    __tablename__ = 'Mission'
    IDMission = db.Column(db.Integer, primary_key=True)
    dateLancement = db.Column(db.DateTime, nullable=False)
    dateCloture = db.Column(db.DateTime, nullable=True)
    estArchivee = db.Column(db.Boolean, default=False)
    responsableMission = db.Column(db.Integer, db.ForeignKey('Employe.IDEmploye', ondelete="SET NULL"), nullable=True)
    clientMission = db.Column(db.Integer, db.ForeignKey('EntrepriseCliente.IDEntreprise', ondelete="CASCADE"), nullable=False)

# ---------------- TRAITEMENT DE DONNES PERSONNELLES ---------------- #
class Traitement(db.Model):
    __tablename__ = 'Traitement'
    IDTraitement = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.String(255), nullable=False)
    finalite = db.Column(db.Text, nullable=False)
    moyensExecution = db.Column(db.Text, nullable=False)
    responsableProcessus = db.Column(db.String(255), nullable=False)
    dateCreation = db.Column(db.DateTime, nullable=False)
    baseLegale = db.Column(db.Text, nullable=False)
    sousTraite = db.Column(db.Boolean, default=False)
    numContratSousTraitant = db.Column(db.String(255), nullable=True)
    typeExecution = db.Column(db.String(255), nullable=False)

# ---------------- SOUS-TRAITANCE ---------------- #
class SousTraitant(db.Model):
    __tablename__ = 'SousTraitant'
    IDSousTraitant = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    prenom = db.Column(db.String(255), nullable=False)
    adresse = db.Column(db.Text, nullable=False)
    numTel = db.Column(db.String(20), nullable=False)
    domaineActivite = db.Column(db.String(255), nullable=False)

# Many-to-Many: Traitement ↔ SousTraitant
SousTraitement = db.Table(
    'SousTraitement',
    db.Column('IDTraitement', db.Integer, db.ForeignKey('Traitement.IDTraitement', ondelete="CASCADE"), primary_key=True),
    db.Column('IDSousTraitant', db.Integer, db.ForeignKey('SousTraitant.IDSousTraitant', ondelete="CASCADE"), primary_key=True)
)

class Clausier(db.Model):
    __tablename__ = 'Clausier'
    IDClausier = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(50), nullable=False)
    sigleSousTraitant = db.Column(db.String(100), nullable=False)
    IDSousTraitant = db.Column(db.Integer, db.ForeignKey('SousTraitant.IDSousTraitant', ondelete="CASCADE"), nullable=False)

# ---------------- ACTIFS SUPPORT ---------------- #
class ActifSupport(db.Model):
    __tablename__ = 'ActifSupport'
    IDActif = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)
    intitule = db.Column(db.String(255), nullable=False)
    srcCollecte = db.Column(db.Text, nullable=False)
    actifCommunique = db.Column(db.Boolean, default=False)
    proprietaireActif = db.Column(db.String(255), nullable=False)
    nbEnregistrementActif = db.Column(db.Integer, nullable=False)
    modeCommunicationTransfert = db.Column(db.String(255), nullable=False)
    objetTransfert = db.Column(db.Text, nullable=False)
    destinataireTransfert = db.Column(db.String(255), nullable=False)
    cadreLegal = db.Column(db.Text, nullable=False)
    rationalBesoin = db.Column(db.Text, nullable=False)
    srcCollecteActif = db.Column(db.Text, nullable=False)
    srcSecondaireCollecteActif = db.Column(db.Text, nullable=True)
    personnelAccesElectronique = db.Column(db.Text, nullable=False)
    emplacementAccesElectronique = db.Column(db.Text, nullable=False)
    personnelAccesPhysique = db.Column(db.Text, nullable=False)
    prestataireAccesElectronique = db.Column(db.Text, nullable=True)
    emplacementPrestataireAccesElect = db.Column(db.Text, nullable=True)
    prestataireAccesPhysique = db.Column(db.Text, nullable=True)
    IDTraitement = db.Column(db.Integer, db.ForeignKey('Traitement.IDTraitement', ondelete="CASCADE"), nullable=False)

# ---------------- STOCKAGE ---------------- #
class MoyenStockage(db.Model):
    __tablename__ = 'MoyenStockage'
    IDMoyenStockage = db.Column(db.Integer, primary_key=True)
    moyenStockage = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('Physique', 'Electronique'), nullable=False)
    nom = db.Column(db.String(255), nullable=False)
    dateCreation = db.Column(db.DateTime, nullable=False)
    taille = db.Column(db.Integer, nullable=False)
    emplacement = db.Column(db.Text, nullable=False)
    dureeRetention = db.Column(db.String(255), nullable=False)
    cadreLegal = db.Column(db.Text, nullable=False)

# Many-to-Many: ActifSupport ↔ MoyenStockage
StockageActif = db.Table(
    'StockageActif',
    db.Column('IDActif', db.Integer, db.ForeignKey('ActifSupport.IDActif', ondelete="CASCADE"), primary_key=True),
    db.Column('IDMoyenStockage', db.Integer, db.ForeignKey('MoyenStockage.IDMoyenStockage', ondelete="CASCADE"), primary_key=True)
)

# ---------------- SECURITE ---------------- #
class MoyenSecurite(db.Model):
    __tablename__ = 'MoyenSecurite'
    IDMoyenSecurite = db.Column(db.Integer, primary_key=True)
    moyenSecurite = db.Column(db.String(255), nullable=False)

# Many-to-Many: ActifSupport ↔ MoyenSecurite
SecuriteActif = db.Table(
    'SecuriteActif',
    db.Column('IDActif', db.Integer, db.ForeignKey('ActifSupport.IDActif', ondelete="CASCADE"), primary_key=True),
    db.Column('IDMoyenSecurite', db.Integer, db.ForeignKey('MoyenSecurite.IDMoyenSecurite', ondelete="CASCADE"), primary_key=True)
)

# ---------------- CATEGORIES PERSONNES & DONNEES ---------------- #
class CategoriePersonne(db.Model):
    __tablename__ = 'CategoriePersonne'
    IDCategoriePersonne = db.Column(db.Integer, primary_key=True)
    categorie = db.Column(db.String(255), nullable=False)

# Many-to-Many: ActifSupport ↔ CategoriePersonne
CategoriePersonneActif = db.Table(
    'CategoriePersonneActif',
    db.Column('IDActif', db.Integer, db.ForeignKey('ActifSupport.IDActif', ondelete="CASCADE"), primary_key=True),
    db.Column('IDCategoriePersonne', db.Integer, db.ForeignKey('CategoriePersonne.IDCategoriePersonne', ondelete="CASCADE"), primary_key=True)
)

class CategorieDonnee(db.Model):
    __tablename__ = 'CategorieDonnee'
    IDCategorieDonnee = db.Column(db.Integer, primary_key=True)
    categorie = db.Column(db.String(255), nullable=False)
    typeDonnee = db.Column(db.String(255), nullable=False)

# Many-to-Many: ActifSupport ↔ CategorieDonnee
CategorieDonneesActif = db.Table(
    'CategorieDonneesActif',
    db.Column('IDActif', db.Integer, db.ForeignKey('ActifSupport.IDActif', ondelete="CASCADE"), primary_key=True),
    db.Column('IDCategorieDonnee', db.Integer, db.ForeignKey('CategorieDonnee.IDCategorieDonnee', ondelete="CASCADE"), primary_key=True)
)


# ---------------- AUDIT & CONFORMITE------- #
class QuestionnaireAudit(db.Model):
    __tablename__ = 'QuestionnaireAudit'
    IDQuestionnaire = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(255), nullable=False)

class Question(db.Model):
    __tablename__ = 'Question'
    IDQuestion = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.Text, nullable=False)
    IDQuestionnaire = db.Column(db.Integer, db.ForeignKey('QuestionnaireAudit.IDQuestionnaire', ondelete="CASCADE"), nullable=False)

class ReponsePossible(db.Model):
    __tablename__ = 'ReponsePossible'
    IDReponsePossible = db.Column(db.Integer, primary_key=True)
    valeur = db.Column(db.String(255), nullable=False)

# Many-to-Many: Question ↔ ReponsePossible
class QuestionReponsePossible(db.Model):
    __tablename__ = 'QuestionReponsePossible'
    IDQuestion = db.Column(db.Integer, db.ForeignKey('Question.IDQuestion', ondelete="CASCADE"), primary_key=True) 
    IDReponsePossible = db.Column(db.Integer, db.ForeignKey('ReponsePossible.IDReponsePossible', ondelete="CASCADE"), primary_key=True) 
    estConforme = db.Column(db.Boolean, nullable=False)
    actionConformite = db.Column(db.Text, nullable=True)

class ReponseUtilisateur(db.Model):
    __tablename__ = 'ReponseUtilisateur'
    IDReponse = db.Column(db.Integer, primary_key=True)
    IDRemplissage = db.Column(db.Integer, db.ForeignKey('RemplissageQuestionnaire.IDRemplissage', ondelete="CASCADE"), nullable=False)
    IDQuestion = db.Column(db.Integer, db.ForeignKey('Question.IDQuestion', ondelete="CASCADE"), nullable=False)
    IDReponsePossible = db.Column(db.Integer, db.ForeignKey('ReponsePossible.IDReponsePossible', ondelete="CASCADE"), nullable=False)


class RemplissageQuestionnaire(db.Model):
    __tablename__ = 'RemplissageQuestionnaire'
    IDRemplissage = db.Column(db.Integer, primary_key=True)
    IDQuestionnaire = db.Column(db.Integer, db.ForeignKey('QuestionnaireAudit.IDQuestionnaire', ondelete="CASCADE"), nullable=False)
    rempliParID = db.Column(db.Integer, db.ForeignKey('Employe.IDEmploye', ondelete="SET NULL"), nullable=True)
    dateRemplissage = db.Column(db.DateTime, nullable=False)
    scoreConformite = db.Column(db.Integer, nullable=False)
    statutConformite = db.Column(db.String(255), nullable=False)

# ---------------- FORMATION & RESOURCES JURIDIQUES ---------------- #
class SupportFormation(db.Model):
    __tablename__ = 'SupportFormation'
    IDSupportFormation = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(255), nullable=False)
    cheminFichier = db.Column(db.Text, nullable=False)

class RessourceJuridique(db.Model):
    __tablename__ = 'RessourceJuridique'
    IDRessource = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(255), nullable=False)
    cheminFichier = db.Column(db.Text, nullable=False)


# ---------------- DEMANDES D'INVOCATION DE DROITS ---------------- #
class DmdInvocationDroit(db.Model):
    __tablename__ = 'DmdInvocationDroit'
    IDDmdDroit = db.Column(db.Integer, primary_key=True)
    dateDmd = db.Column(db.DateTime, nullable=False)
    faiteParPersonneConcernee = db.Column(db.Boolean, default=False)
    natureRequete = db.Column(db.String(255), nullable=False)
    natureDmd = db.Column(db.String(255), nullable=False)
    motifDmd = db.Column(db.Text, nullable=False)
    demandeSignee = db.Column(db.Boolean, default=False)
    statut = db.Column(db.String(255), nullable=False)
    motifRefus = db.Column(db.Text, nullable=True)
    IDDemandeur = db.Column(db.Integer, db.ForeignKey('Demandeur.IDDemandeur', ondelete="CASCADE"), nullable=False)
    IDPersonneConcernee = db.Column(db.Integer, db.ForeignKey('PersonneConcernee.IDPersonneConcernee', ondelete="CASCADE"), nullable=False)
    IDMission = db.Column(db.Integer, db.ForeignKey('Mission.IDMission', ondelete="CASCADE"), nullable=False)

class Demandeur(db.Model):
    __tablename__ = 'Demandeur'
    IDDemandeur = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    prenom = db.Column(db.String(255), nullable=False)
    numTel = db.Column(db.String(20), nullable=False)
    adresseMail = db.Column(db.String(255), nullable=False)
    natureRelationAvecPC = db.Column(db.String(255), nullable=False)

class PersonneConcernee(db.Model):
    __tablename__ = 'PersonneConcernee'
    IDPersonneConcernee = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    prenom = db.Column(db.String(255), nullable=False)
    numTel = db.Column(db.String(20), nullable=False)
    adresseMail = db.Column(db.String(255), nullable=False)
    adresse = db.Column(db.Text, nullable=False)
    matricule = db.Column(db.String(255), nullable=False)
    natureRelationEntreprise = db.Column(db.String(255), nullable=False)

# ---------------- ACTIONS DE TRAITEMENT DES DEMANDES ---------------- #
class ActionTraitementDmd(db.Model):
    __tablename__ = 'ActionTraitementDmd'
    IDAction = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    responsable = db.Column(db.Integer, db.ForeignKey('Employe.IDEmploye', ondelete="SET NULL"), nullable=True)
    dateCreation = db.Column(db.DateTime, nullable=False)
    dateDebut = db.Column(db.DateTime, nullable=False)
    dateFin = db.Column(db.DateTime, nullable=False)
    statut = db.Column(db.String(255), nullable=False)
    commentaire = db.Column(db.Text, nullable=True)
    IDDmdDroit = db.Column(db.Integer, db.ForeignKey('DmdInvocationDroit.IDDmdDroit', ondelete="CASCADE"), nullable=False)

# ---------------- LETTRES DE REPONSE ---------------- #
class LettreReponse(db.Model):
    __tablename__ = 'LettreReponse'
    IDLettreReponse = db.Column(db.Integer, primary_key=True)
    dmdAcceptee = db.Column(db.Boolean, default=False)
    contenuLettre = db.Column(db.Text, nullable=False)
    IDDmdDroit = db.Column(db.Integer, db.ForeignKey('DmdInvocationDroit.IDDmdDroit', ondelete="CASCADE"), nullable=False)  

# ---------------- NOTICES D'INFORMATION ---------------- #
class NoticeInformation(db.Model):
    __tablename__ = 'NoticeInformation'
    IDNoticeInfo = db.Column(db.Integer, primary_key=True)
    dateCreation = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(50), nullable=False)
    contenuFR = db.Column(db.Text, nullable=False)
    contenuAR = db.Column(db.Text, nullable=False)
    estUnTemplate = db.Column(db.Boolean, default=False)
    categoriePersonneConcernee = db.Column(db.String(255), nullable=False)
    IDMission = db.Column(db.Integer, db.ForeignKey('Mission.IDMission', ondelete="CASCADE"), nullable=False)

# ---------------- CONSENTEMENTS ---------------- #
class Consentement(db.Model):
    __tablename__ = 'Consentement'
    IDConsentement = db.Column(db.Integer, primary_key=True)
    estSigne = db.Column(db.Boolean, default=False)
    dateSignature = db.Column(db.DateTime, nullable=False)
    IDPersonneConcernee = db.Column(db.Integer, db.ForeignKey('PersonneConcernee.IDPersonneConcernee', ondelete="CASCADE"), nullable=False)
    IDNotice = db.Column(db.Integer, db.ForeignKey('NoticeInformation.IDNoticeInfo', ondelete="CASCADE"), nullable=False)

# ---------------- INCIDENTS ---------------- #
class Incident(db.Model):
    __tablename__ = 'Incident'
    IDIncident = db.Column(db.Integer, primary_key=True)
    typeIncident = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    dateSignalement = db.Column(db.DateTime, nullable=False)
    IDMission = db.Column(db.Integer, db.ForeignKey('Mission.IDMission', ondelete="CASCADE"), nullable=False)
    signaleParID = db.Column(db.Integer, db.ForeignKey('Employe.IDEmploye', ondelete="SET NULL"), nullable=True)

# ---------------- FORMATION & RESSOURCES JURIDIQUES ---------------- #
# Many-to-Many: SupportFormation ↔ Mission
FormationMission = db.Table(
    'FormationMission',
    db.Column('IDSupportFormation', db.Integer, db.ForeignKey('SupportFormation.IDSupportFormation', ondelete="CASCADE"), primary_key=True),
    db.Column('IDMission', db.Integer, db.ForeignKey('Mission.IDMission', ondelete="CASCADE"), primary_key=True)
)

# Many-to-Many: RessourceJuridique ↔ Mission
RessourceMission = db.Table(
    'RessourceMission',
    db.Column('IDRessource', db.Integer, db.ForeignKey('RessourceJuridique.IDRessource', ondelete="CASCADE"), primary_key=True),
    db.Column('IDMission', db.Integer, db.ForeignKey('Mission.IDMission', ondelete="CASCADE"), primary_key=True) 
)