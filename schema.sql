DROP TABLE form_entry;
DROP TABLE category;


CREATE TABLE IF NOT EXISTS category (
category_id INTEGER PRIMARY KEY AUTOINCREMENT,
category_label TEXT NOT NULL,
category_exclusive BOOLEAN NOT NULL,
category_order INTEGER DEFAULT 0,
category_last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);


CREATE TABLE IF NOT EXISTS form_entry (
    form_entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    form_entry_label TEXT NOT NULL,
    form_entry_instruction TEXT NOT NULL,
    form_entry_order INTEGER DEFAULT 0,
    form_entry_last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(category_id) REFERENCES category(category_id)
);

insert into category(category_label,category_exclusive,category_order) values('attitude en classe',True,1);
insert into form_entry(category_id,form_entry_label,form_entry_instruction,form_entry_order) values(1,'bon','qui fait preuve d''une bonne attitude en classe',1);
insert into form_entry(category_id,form_entry_label,form_entry_instruction,form_entry_order) values(1,'tres bon','qui fait preuve d''une tres bonne attitude en classe',2);

insert into category(category_label,category_exclusive,category_order) values('participation orale',True,2);
insert into form_entry(category_id,form_entry_label,form_entry_instruction,form_entry_order) values(2,'active','dont la participation orale pourrait etre plus active',1);
insert into form_entry(category_id,form_entry_label,form_entry_instruction,form_entry_order) values(2,'encourage','que j''encourage a participer d''avantage',2);
insert into form_entry(category_id,form_entry_label,form_entry_instruction,form_entry_order) values(2,'concentration','pour qui un peu plus de participation orale et de concentration en classe l''aideraient a progresser d''avantage',3);

insert into category(category_label,category_exclusive,category_order) values('confiance',True,3);
insert into category(category_label,category_exclusive,category_order) values('concentration',True,4);
insert into category(category_label,category_exclusive,category_order) values('approfondissement',False,5);
insert into form_entry(category_id,form_entry_label,form_entry_instruction,form_entry_order) values(5,'pb','qui doit renforcer la resolution de problemes',1);
insert into form_entry(category_id,form_entry_label,form_entry_instruction,form_entry_order) values(5,'calcul mental','qui doit renforcer le calcul mental',2);
insert into form_entry(category_id,form_entry_label,form_entry_instruction,form_entry_order) values(5,'comp. lecture','qui doit approfondir la comprehension de lecture',2);