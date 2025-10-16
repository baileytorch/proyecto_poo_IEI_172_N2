USE iei_172_n2;

ALTER TABLE modelos ADD COLUMN id_marca INTEGER NOT NULL;
ALTER TABLE modelos ADD CONSTRAINT fk_modelos_marcas FOREIGN KEY (id_marca) REFERENCES marcas(id);