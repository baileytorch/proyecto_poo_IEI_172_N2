USE iei_172_n2;

CREATE TABLE IF NOT EXISTS comunas(
    id INTEGER AUTO_INCREMENT,
    codigo_comuna CHAR(5) NOT NULL,
    nombre_comuna VARCHAR(60) NOT NULL,

    CONSTRAINT pk_comunas PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS direcciones(
    id INTEGER AUTO_INCREMENT,
    calle VARCHAR(255) NULL,
    numero VARCHAR(10) NULL,
    departamento VARCHAR(10) NULL,
    detalles VARCHAR(255) NULL,
    id_comuna INTEGER NOT NULL,

    CONSTRAINT pk_direcciones PRIMARY KEY (id),
    CONSTRAINT fk_direcciones_comunas FOREIGN KEY (id_comuna) REFERENCES comunas(id)
);