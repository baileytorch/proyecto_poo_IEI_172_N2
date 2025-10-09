USE iei_172_n2;

CREATE TABLE IF NOT EXISTS comunas (
    id INTEGER AUTO_INCREMENT,
    codigo_comuna CHAR(5) NOT NULL,
    nombre_comuna VARCHAR(60) NOT NULL,

    CONSTRAINT pk_comunas PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS direcciones (
    id INTEGER AUTO_INCREMENT,
    calle VARCHAR(255) NULL,
    numero VARCHAR(10) NULL,
    departamento VARCHAR(10) NULL,
    detalles VARCHAR(255) NULL,
    id_comuna INTEGER NOT NULL,

    CONSTRAINT pk_direcciones PRIMARY KEY (id),
    CONSTRAINT fk_direcciones_comunas FOREIGN KEY (id_comuna) REFERENCES comunas(id)
);

CREATE TABLE IF NOT EXISTS talleres (
    id INT AUTO_INCREMENT,
    nombre_taller VARCHAR(50) NOT NULL,
    direccion_taller INT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_talleres PRIMARY KEY (id),
    CONSTRAINT fk_talleres_direcciones FOREIGN KEY (direccion_taller) REFERENCES direcciones(id)
);

CREATE TABLE IF NOT EXISTS tipos_mecanico (
    id INT AUTO_INCREMENT,
    tipo_mecanico VARCHAR(50) NOT NULL,
    descripcion_tipo_mecanico VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_tipos_mecanico PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS mecanicos (
    id INT AUTO_INCREMENT,
    rut_mecanico CHAR(10) NOT NULL UNIQUE,
    nombre_mecanico VARCHAR(100) NOT NULL,
    fecha_contrato DATE NOT NULL,
    salario_mecanico FLOAT NULL,
    telefono_mecanico VARCHAR(12) NULL,
    fecha_nacimiento_mecanico DATE NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    tipo_mecanico INT NOT NULL,
    direccion_mecanico INT NULL,

    CONSTRAINT pk_mecanicos PRIMARY KEY (id),
    CONSTRAINT fk_mecanicos_tipos_mecanico FOREIGN KEY (tipo_mecanico) REFERENCES tipos_mecanico(id),
    CONSTRAINT fk_mecanicos_direcciones FOREIGN KEY (direccion_mecanico) REFERENCES direcciones(id)
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) NULL,
    contrasena_usuario VARCHAR(50) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    id_mecanico INT NOT NULL,

    CONSTRAINT pk_usuarios PRIMARY KEY (id),
    CONSTRAINT fk_usuarios_mecanicos FOREIGN KEY (id_mecanico) REFERENCES mecanicos(id)
);

CREATE TABLE IF NOT EXISTS mecanicos_taller (
    id INT AUTO_INCREMENT,
    habilitado TINYINT NOT NULL DEFAULT 1,
    id_mecanico INT NOT NULL,
    id_taller INT NOT NULL,

    CONSTRAINT pk_mecanicos_taller PRIMARY KEY (id),
    CONSTRAINT fk_mecanicos_taller_mecanicos FOREIGN KEY (id_mecanico) REFERENCES mecanicos(id),
    CONSTRAINT fk_mecanicos_taller_talleres FOREIGN KEY (id_taller) REFERENCES talleres(id)
);

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT,
    rut_cliente VARCHAR(10) NULL,
    razon_social VARCHAR(255) NOT NULL,
    correo_contacto VARCHAR(255) NULL,
    telefono_contacto VARCHAR(12) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    id_direccion INT NULL,

    CONSTRAINT pk_clientes PRIMARY KEY (id),
    CONSTRAINT fk_clientes_direcciones FOREIGN KEY (id_direccion) REFERENCES direcciones(id)
);

CREATE TABLE IF NOT EXISTS combustibles(
    id INT AUTO_INCREMENT,
    tipo_combustible VARCHAR(25),
    descripcion_tipo_combustible VARCHAR(255),

    CONSTRAINT pk_combustible PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS marcas(
    id INT AUTO_INCREMENT,
    nombre_marca VARCHAR(25) NOT NULL,
    pais_origen VARCHAR(50) NULL,

    CONSTRAINT pk_marcas PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS modelos(
    id INT AUTO_INCREMENT,
    nombre_modelo VARCHAR(25) NOT NULL,
    descripcion_modelo VARCHAR(255) NULL,
    tipo_combustible INT NOT NULL,
    puertas INT NOT NULL,

    CONSTRAINT pk_modelos PRIMARY KEY (id),
    CONSTRAINT fk_modelos_combustibles FOREIGN KEY (tipo_combustible) REFERENCES combustibles(id)
);

CREATE TABLE IF NOT EXISTS tipos_vehiculo(
    id INT AUTO_INCREMENT,
    tipo_vehiculo VARCHAR(25) NOT NULL,
    descripcion_tipo_vehiculo VARCHAR(255) NULL,

    CONSTRAINT pk_tipos_vehiculo PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS vehiculos (
    id INT AUTO_INCREMENT,
    anio_vehiculo CHAR(4) NULL,
    patente_vehiculo CHAR(7) NULL,
    color_vehiculo VARCHAR(25) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    modelo_vehiculo INT NOT NULL,
    tipo_vehiculo INT NOT NULL,

    CONSTRAINT pk_vehiculos PRIMARY KEY (id),
    CONSTRAINT fk_vehiculos_modelos FOREIGN KEY (modelo_vehiculo) REFERENCES modelos(id),
    CONSTRAINT fk_vehiculos_tipos_vehiculo FOREIGN KEY (tipo_vehiculo) REFERENCES tipos_vehiculo(id)
);

CREATE TABLE IF NOT EXISTS vehiculos_cliente (
    id INT AUTO_INCREMENT,
    id_vehiculo INT NOT NULL,
    id_cliente INT NOT NULL,
    id_taller INT NOT NULL,

    CONSTRAINT pk_vehiculos_cliente PRIMARY KEY (id),
    CONSTRAINT fk_vehiculos_cliente_vehiculos FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id),
    CONSTRAINT fk_vehiculos_cliente_clientes FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    CONSTRAINT fk_vehiculos_cliente_talleres FOREIGN KEY (id_taller) REFERENCES talleres(id)
);

CREATE TABLE IF NOT EXISTS reparaciones (
    id INT AUTO_INCREMENT,
    motivo_ingreso VARCHAR(255) NOT NULL,
    fecha_ingreso DATETIME NOT NULL,
    fecha_entrega DATETIME NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    id_ingreso INT NOT NULL,

    CONSTRAINT pk_reparaciones PRIMARY KEY (id),
    CONSTRAINT fk_reparaciones_vehiculos_cliente FOREIGN KEY (id_ingreso) REFERENCES vehiculos_cliente(id)
);

CREATE TABLE IF NOT EXISTS detalle_reparaciones (
    id INT AUTO_INCREMENT,
    detalle_reparacion VARCHAR(255) NOT NULL,
    requiere_repuestos TINYINT NOT NULL DEFAULT 1,
    autorizado TINYINT NOT NULL DEFAULT 1,
    id_reparacion INT NOT NULL,

    CONSTRAINT pk_detalle_reparaciones PRIMARY KEY (id),
    CONSTRAINT fk_detalle_reparaciones_reparaciones FOREIGN KEY (id_reparacion) REFERENCES reparaciones(id)
);

CREATE TABLE IF NOT EXISTS repuestos (
    id INT AUTO_INCREMENT,
    fecha_registro DATETIME NOT NULL,
    detalles_repuesto VARCHAR(255) NULL,
    valor_repuesto FLOAT NULL,
    id_detalle_reparacion INT NOT NULL,

    CONSTRAINT pk_repuestos PRIMARY KEY (id),
    CONSTRAINT fk_repuestos FOREIGN KEY (id_detalle_reparacion) REFERENCES detalle_reparaciones(id)
);