Le site implémente un systeme de d'authentification avec controle de session. Dès la connection on peut visualiser les utiliateurs présent dans la base de donnée

commande dans la BDD: 

CREATE USER 'louis'@'localhost' IDENTIFIED BY 'louis';
GRANT ALL PRIVILEGES ON identity.* TO 'louis'@'localhost';
GRANT ALL PRIVILEGES ON identity.* TO 'config_generator'@'localhost';
INSERT INTO user (nom, prenom, email, telephone, date_naissance) VALUES ('Dupont', 'Jean', 'jean.dupont@email.com', '0123456789', '1990-01-01');
INSERT INTO user (nom, prenom, email, telephone, date_naissance) VALUES ('Dupond', 'stan', 'stan.dupont@email.com', '9876543210', '2000-05-01');

CREATE TABLE user (
    iduser INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    email VARCHAR(255),
    telephone VARCHAR(255),
    date_naissance DATE,
    UNIQUE (iduser)
) ENGINE=InnoDB;

CREATE TABLE auth (
    idauth INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(255),
    password VARCHAR(255),
    iduser INT,
    FOREIGN KEY (iduser) REFERENCES user(iduser)
);



CREATE TABLE server (
    idserver INT AUTO_INCREMENT PRIMARY KEY,
    page_default VARCHAR(255),
    dossier_site VARCHAR(255),
    dossier_erreur VARCHAR(255),
    UNIQUE (idserver)
);

CREATE TABLE loadbalancer (
    idloadB INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    location VARCHAR(255),
    dossierLB VARCHAR(255),
    idserver INT,
    FOREIGN KEY (idserver) REFERENCES server(idserver)
);

CREATE TABLE reverse_proxy (
    idReverseP INT AUTO_INCREMENT PRIMARY KEY,
    proxy_bind VARCHAR(255),
    proxy_pass VARCHAR(255),
    dossierServerP VARCHAR(255),
    nom VARCHAR(255),
    UNIQUE (idReverseP)
);

Merci !
