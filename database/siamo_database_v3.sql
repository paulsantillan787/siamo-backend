
CREATE TABLE Automovil
(
  id_automovil int         NOT NULL GENERATED ALWAYS AS IDENTITY,
  placa        varchar(8)  NOT NULL,
  marca        varchar(15) NOT NULL,
  modelo       varchar(50) NOT NULL,
  id_cliente   int         NOT NULL,
  PRIMARY KEY (id_automovil)
);

COMMENT ON COLUMN Automovil.placa IS 'número';

CREATE TABLE Cliente
(
  id_cliente int NOT NULL GENERATED ALWAYS AS IDENTITY,
  id_persona int NOT NULL,
  PRIMARY KEY (id_cliente)
);

CREATE TABLE Consulta
(
  id_consulta    int          NOT NULL GENERATED ALWAYS AS IDENTITY,
  cod_consulta   int          NOT NULL,
  id_cliente     int          NOT NULL,
  prob_declarado varchar(200) NOT NULL,
  id_tecnico     int          NOT NULL,
  estado         int          NOT NULL DEFAULT 1,
  id_automovil   int          NOT NULL,
  PRIMARY KEY (id_consulta)
);

COMMENT ON COLUMN Consulta.id_consulta IS 'a nivel sistema';

COMMENT ON COLUMN Consulta.cod_consulta IS 'para búsqueda';

COMMENT ON COLUMN Consulta.prob_declarado IS 'por el cliente';

COMMENT ON COLUMN Consulta.id_tecnico IS 'diagnostico inicial';

COMMENT ON COLUMN Consulta.estado IS '1: en espera, 2: cancelado, 3: procede';

CREATE TABLE Empleado
(
  id_empleado   int          NOT NULL GENERATED ALWAYS AS IDENTITY,
  id_persona    int          NOT NULL,
  fecha_ingreso date         NOT NULL,
  cod_empleado  int          NOT NULL,
  contrasenia   varchar(255) NOT NULL,
  PRIMARY KEY (id_empleado)
);

COMMENT ON COLUMN Empleado.id_empleado IS 'privado';

COMMENT ON COLUMN Empleado.fecha_ingreso IS 'contratación';

COMMENT ON COLUMN Empleado.cod_empleado IS 'público (inicio sesión)';

COMMENT ON COLUMN Empleado.contrasenia IS 'encriptada';

CREATE TABLE Estado_vehiculo
(
  id_estado_vehiculo int          NOT NULL GENERATED ALWAYS AS IDENTITY,
  estado_carroceria  varchar(200) NOT NULL,
  estado_neumaticos  varchar(200) NOT NULL,
  estado_motor       varchar(200) NOT NULL,
  estado_frenos      varchar(200) NOT NULL,
  id_ficha_ingreso   int          NOT NULL,
  PRIMARY KEY (id_estado_vehiculo)
);

COMMENT ON TABLE Estado_vehiculo IS 'inventario pre internacion';

CREATE TABLE Ficha_ingreso
(
  id_ficha_ingreso     int       NOT NULL GENERATED ALWAYS AS IDENTITY,
  fecha_ingreso        timestamp NOT NULL,
  fecha_recogida_aprox timestamp NOT NULL,
  id_ost               int       NOT NULL,
  PRIMARY KEY (id_ficha_ingreso)
);

COMMENT ON COLUMN Ficha_ingreso.fecha_ingreso IS 'YYYY-MM-DD hh:mm:ss';

COMMENT ON COLUMN Ficha_ingreso.fecha_recogida_aprox IS 'YYYY-MM-DD hh:mm:ss';

CREATE TABLE Ficha_salida
(
  id_ficha_salida int       NOT NULL GENERATED ALWAYS AS IDENTITY,
  fecha_recojo    timestamp NOT NULL,
  id_ost          int       NOT NULL,
  PRIMARY KEY (id_ficha_salida)
);

COMMENT ON COLUMN Ficha_salida.fecha_recojo IS 'YYYY-MM-DD hh:mm:ss';

CREATE TABLE Imprevisto
(
  id_imprevisto int          NOT NULL GENERATED ALWAYS AS IDENTITY,
  descripcion   varchar(300) NOT NULL,
  solucion      varchar(300) NOT NULL,
  precio        float        NOT NULL,
  estado        int          NOT NULL DEFAULT 1,
  PRIMARY KEY (id_imprevisto)
);

COMMENT ON COLUMN Imprevisto.solucion IS 'propuesta';

COMMENT ON COLUMN Imprevisto.estado IS '1: considerado, 2: no considerado';

CREATE TABLE Informe_tecnico
(
  id_informe_tecnico      int          NOT NULL,
  id_ost                  int          NOT NULL,
  fecha_inicio_reparacion date        ,
  fecha_fin_reparacion    date        ,
  saldo_final             float       ,
  detalle_reparacion      varchar(250),
  observaciones           varchar(300),
  id_imprevisto           int          NOT NULL,
  PRIMARY KEY (id_informe_tecnico)
);

COMMENT ON COLUMN Informe_tecnico.fecha_inicio_reparacion IS 'YYYY-MM-DD';

COMMENT ON COLUMN Informe_tecnico.saldo_final IS 'incluye imprevistos';

COMMENT ON COLUMN Informe_tecnico.detalle_reparacion IS 'para el cliente';

CREATE TABLE Lista_problemas
(
  id_consulta int NOT NULL,
  id_problema int NOT NULL,
  PRIMARY KEY (id_consulta, id_problema)
);

COMMENT ON TABLE Lista_problemas IS 'por el tecnico';

CREATE TABLE Lista_tareas
(
  id_lista_tareas int NOT NULL GENERATED ALWAYS AS IDENTITY,
  id_ost          int NOT NULL,
  PRIMARY KEY (id_lista_tareas)
);

CREATE TABLE Orden_Servicio_Tecnico
(
  id_ost              int  NOT NULL GENERATED ALWAYS AS IDENTITY,
  cod_ost             int  NOT NULL,
  fecha_registro      date NOT NULL,
  estado              int  NOT NULL DEFAULT 1,
  id_consulta         int  NOT NULL,
  fecha_aprox_ingreso date NOT NULL,
  PRIMARY KEY (id_ost)
);

COMMENT ON COLUMN Orden_Servicio_Tecnico.id_ost IS 'a nivel de sistema';

COMMENT ON COLUMN Orden_Servicio_Tecnico.cod_ost IS 'para búsqueda';

COMMENT ON COLUMN Orden_Servicio_Tecnico.fecha_registro IS 'definido automáticamente';

COMMENT ON COLUMN Orden_Servicio_Tecnico.estado IS '1: en proceso, 2: resuelto, 3: cancelado, 4: abandonado';

COMMENT ON COLUMN Orden_Servicio_Tecnico.fecha_aprox_ingreso IS 'YYYY-MM-DD';

CREATE TABLE Persona
(
  id_persona int          NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombres    varchar(30)  NOT NULL,
  apellidos  varchar(50)  NOT NULL,
  tipo_doc   int          NOT NULL,
  num_doc    varchar(11)  NOT NULL UNIQUE,
  direccion  varchar(100) NOT NULL,
  correo     varchar(50)  NOT NULL,
  telefono   varchar(9)   NOT NULL,
  sexo       char(1)      NOT NULL,
  PRIMARY KEY (id_persona)
);

COMMENT ON COLUMN Persona.tipo_doc IS '1: dni, 2: carnet extranjería';

COMMENT ON COLUMN Persona.num_doc IS '8 para dni y 11 para carnet extranjería';

COMMENT ON COLUMN Persona.telefono IS 'solo en Perú';

COMMENT ON COLUMN Persona.sexo IS 'F: femenino, M: masculino';

CREATE TABLE Presupuesto
(
  id_presupuesto      int   NOT NULL GENERATED ALWAYS AS IDENTITY,
  id_consulta         int   NOT NULL,
  tarifa_mano_obra    float NOT NULL,
  tarifa_repuestos    float NOT NULL DEFAULT 0,
  descuento_negociado float NOT NULL DEFAULT 0,
  PRIMARY KEY (id_presupuesto)
);

COMMENT ON COLUMN Presupuesto.tarifa_mano_obra IS 'segun n tecnicos y complejidad';

CREATE TABLE Presupuesto_repuesto
(
  id_presupuesto int NOT NULL,
  id_repuesto    int NOT NULL,
  cantidad       int NOT NULL DEFAULT 1,
  PRIMARY KEY (id_presupuesto, id_repuesto)
);

CREATE TABLE Problema
(
  id_problema int          NOT NULL GENERATED ALWAYS AS IDENTITY,
  id_solucion int          NOT NULL,
  descripcion varchar(50)  NOT NULL UNIQUE,
  detalle     varchar(250) NOT NULL,
  PRIMARY KEY (id_problema)
);

COMMENT ON TABLE Problema IS 'bitacora';

COMMENT ON COLUMN Problema.descripcion IS 'breve';

CREATE TABLE Recepcionista
(
  id_recepcionista int NOT NULL GENERATED ALWAYS AS IDENTITY,
  id_empleado      int NOT NULL,
  PRIMARY KEY (id_recepcionista)
);

CREATE TABLE Repuesto
(
  id_repuesto int         NOT NULL GENERATED ALWAYS AS IDENTITY,
  descripcion varchar(50) NOT NULL UNIQUE,
  precio      float       NOT NULL,
  PRIMARY KEY (id_repuesto)
);

CREATE TABLE Solucion
(
  id_solucion int          NOT NULL GENERATED ALWAYS AS IDENTITY,
  descripcion varchar(250) NOT NULL,
  PRIMARY KEY (id_solucion)
);

COMMENT ON TABLE Solucion IS 'bitacora';

CREATE TABLE Tarea
(
  id_tarea        int         NOT NULL GENERATED ALWAYS AS IDENTITY,
  descripcion     varchar(50) NOT NULL,
  id_lista_tareas int         NOT NULL,
  id_tecnico      int         NOT NULL,
  estado          int         NOT NULL DEFAULT 1,
  PRIMARY KEY (id_tarea)
);

COMMENT ON COLUMN Tarea.estado IS '1: no resuelta, 2: resuelta';

CREATE TABLE Tecnico
(
  id_tecnico  int NOT NULL GENERATED ALWAYS AS IDENTITY,
  id_empleado int NOT NULL,
  PRIMARY KEY (id_tecnico)
);

ALTER TABLE Cliente
  ADD CONSTRAINT FK_Persona_TO_Cliente
    FOREIGN KEY (id_persona)
    REFERENCES Persona (id_persona);

ALTER TABLE Empleado
  ADD CONSTRAINT FK_Persona_TO_Empleado
    FOREIGN KEY (id_persona)
    REFERENCES Persona (id_persona);

ALTER TABLE Recepcionista
  ADD CONSTRAINT FK_Empleado_TO_Recepcionista
    FOREIGN KEY (id_empleado)
    REFERENCES Empleado (id_empleado);

ALTER TABLE Tecnico
  ADD CONSTRAINT FK_Empleado_TO_Tecnico
    FOREIGN KEY (id_empleado)
    REFERENCES Empleado (id_empleado);

ALTER TABLE Informe_tecnico
  ADD CONSTRAINT FK_Orden_Servicio_Tecnico_TO_Informe_tecnico
    FOREIGN KEY (id_ost)
    REFERENCES Orden_Servicio_Tecnico (id_ost);

ALTER TABLE Automovil
  ADD CONSTRAINT FK_Cliente_TO_Automovil
    FOREIGN KEY (id_cliente)
    REFERENCES Cliente (id_cliente);

ALTER TABLE Consulta
  ADD CONSTRAINT FK_Cliente_TO_Consulta
    FOREIGN KEY (id_cliente)
    REFERENCES Cliente (id_cliente);

ALTER TABLE Consulta
  ADD CONSTRAINT FK_Tecnico_TO_Consulta
    FOREIGN KEY (id_tecnico)
    REFERENCES Tecnico (id_tecnico);

ALTER TABLE Lista_problemas
  ADD CONSTRAINT FK_Consulta_TO_Lista_problemas
    FOREIGN KEY (id_consulta)
    REFERENCES Consulta (id_consulta);

ALTER TABLE Lista_problemas
  ADD CONSTRAINT FK_Problema_TO_Lista_problemas
    FOREIGN KEY (id_problema)
    REFERENCES Problema (id_problema);

ALTER TABLE Problema
  ADD CONSTRAINT FK_Solucion_TO_Problema
    FOREIGN KEY (id_solucion)
    REFERENCES Solucion (id_solucion);

ALTER TABLE Presupuesto_repuesto
  ADD CONSTRAINT FK_Presupuesto_TO_Presupuesto_repuesto
    FOREIGN KEY (id_presupuesto)
    REFERENCES Presupuesto (id_presupuesto);

ALTER TABLE Presupuesto_repuesto
  ADD CONSTRAINT FK_Repuesto_TO_Presupuesto_repuesto
    FOREIGN KEY (id_repuesto)
    REFERENCES Repuesto (id_repuesto);

ALTER TABLE Presupuesto
  ADD CONSTRAINT FK_Consulta_TO_Presupuesto
    FOREIGN KEY (id_consulta)
    REFERENCES Consulta (id_consulta);

ALTER TABLE Lista_tareas
  ADD CONSTRAINT FK_Orden_Servicio_Tecnico_TO_Lista_tareas
    FOREIGN KEY (id_ost)
    REFERENCES Orden_Servicio_Tecnico (id_ost);

ALTER TABLE Tarea
  ADD CONSTRAINT FK_Lista_tareas_TO_Tarea
    FOREIGN KEY (id_lista_tareas)
    REFERENCES Lista_tareas (id_lista_tareas);

ALTER TABLE Tarea
  ADD CONSTRAINT FK_Tecnico_TO_Tarea
    FOREIGN KEY (id_tecnico)
    REFERENCES Tecnico (id_tecnico);

ALTER TABLE Orden_Servicio_Tecnico
  ADD CONSTRAINT FK_Consulta_TO_Orden_Servicio_Tecnico
    FOREIGN KEY (id_consulta)
    REFERENCES Consulta (id_consulta);

ALTER TABLE Informe_tecnico
  ADD CONSTRAINT FK_Imprevisto_TO_Informe_tecnico
    FOREIGN KEY (id_imprevisto)
    REFERENCES Imprevisto (id_imprevisto);

ALTER TABLE Ficha_salida
  ADD CONSTRAINT FK_Orden_Servicio_Tecnico_TO_Ficha_salida
    FOREIGN KEY (id_ost)
    REFERENCES Orden_Servicio_Tecnico (id_ost);

ALTER TABLE Ficha_ingreso
  ADD CONSTRAINT FK_Orden_Servicio_Tecnico_TO_Ficha_ingreso
    FOREIGN KEY (id_ost)
    REFERENCES Orden_Servicio_Tecnico (id_ost);

ALTER TABLE Estado_vehiculo
  ADD CONSTRAINT FK_Ficha_ingreso_TO_Estado_vehiculo
    FOREIGN KEY (id_ficha_ingreso)
    REFERENCES Ficha_ingreso (id_ficha_ingreso);

ALTER TABLE Consulta
  ADD CONSTRAINT FK_Automovil_TO_Consulta
    FOREIGN KEY (id_automovil)
    REFERENCES Automovil (id_automovil);

CREATE UNIQUE INDEX id_persona
  ON Persona (id_persona ASC);

CREATE UNIQUE INDEX id_cliente
  ON Cliente (id_cliente ASC);

CREATE UNIQUE INDEX id_empleado
  ON Empleado (id_empleado ASC);

CREATE UNIQUE INDEX id_recepcionista
  ON Recepcionista (id_recepcionista ASC);

CREATE UNIQUE INDEX id_tecnico
  ON Tecnico (id_tecnico ASC);

CREATE UNIQUE INDEX id_ost
  ON Orden_Servicio_Tecnico (id_ost ASC);

CREATE UNIQUE INDEX id_detalle_ost
  ON Informe_tecnico (id_informe_tecnico ASC);

CREATE UNIQUE INDEX id_problema
  ON Problema (id_problema ASC);

CREATE UNIQUE INDEX id_solucion
  ON Solucion (id_solucion ASC);
