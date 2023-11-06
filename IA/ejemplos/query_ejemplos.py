Q_EJEMPLOS = {"Consejo Constitucional de Chile" :'''
<<<Proceso actual>>>
(kastitucion OR chanchullo OR mamarrachofacho OR (consej* NEAR/0f constitu*) OR (enmiend* NEAR/0f (aprobad* OR rechaz* OR propuest*)) OR ((retir* OR aprob* OR aprueb* OR rechaz*) NEAR/0f (enmiend* OR norma)) OR "una que nos hunda" OR "una que nos una" OR (nueva NEAR/0f constitucion) OR (comision NEAR/0f experta) OR "vamos a decir que no" OR (Constitucion* NEAR/2f (coludido* OR ricos OR privilegiad*)) OR mamarracho OR laweatambienesmala OR quedopeor OR laweaesmala OR (quedo NEAR/0f peor))
<<<Proceso anterior>>>
 OR ((convencion NEAR/0f constitu*) OR "4s" OR exconstituyente OR mamarracho)
 <<<Hashtags>>>
OR (#tequierochile OR #consejoconstitucional OR #procesoconstitucional OR #vamosadecirqueno OR #chilerechazadosveces OR #rechazolakastitucion OR #encontra OR #afavor OR #encontraendiciembre OR #chilevotaencontra OR #unaquenosuna OR #unaquenoshunda OR #circoconstituyente  OR #rechazo OR #feliz4deseptiembre OR #apruebo OR #4septiembre OR #aniversario4s OR #soloquedarepublicanos OR #nuevaconstitucion OR #laconstituciondelasfakenews OR #4deseptiembre OR #rechazodesalida OR #rechazoendiciembre OR #enmienda* OR #endiciembrevotaencontra OR #afavorendiciembre OR #paravivirseguros OR #afavordechile OR #encontraendiciembre OR #chilevotaencontra OR #encontraatodoevento OR #esmejor)

OR

author:(joseantoniokast OR
rojoedwards	OR
CarmenAravenaA1	OR
BarchiesiDip	OR
sanchezdiputado	OR
agustinromerole	OR
JoseMezaPereira	OR
cristian_arayal	OR
JIrarrazavalR	OR
BenjaminMorenob	OR
DipCristobal	OR
SchubertRubio	OR
mauricio_ojedar	OR
hjurgensen	OR
arturo_squella	OR
ruth_uas	OR
NinoskaPayauna	OR
spg319	OR
CarmenM05875475	OR
carlossolarb	OR
PaulSfeir	OR
gloriaparedesAB	OR
angeleslpo	OR
abarchiesi	OR
profesor_silva	OR
JorgeOssandonRM	OR
safigueroa	OR
idilia_maria	OR
ricardortegapr	OR
MiguelRojasCL	OR
ceciliamedinam4	OR
SpoererPatricia	OR
AldoSanhueza	OR
marielaandreafm	OR
HectorUrbanA	OR
JorgeDelaMaza22	OR
beaheviaw)

OR

<<<Migrantes>>>
(enmiend* NEAR/3f ((expuls* NEAR/2f (inmediata OR migrant*)) OR ((norma* OR enmienda*) NEAR/1f ((anti NEAR/0f migrante*) OR antimigrante* OR "anti-migrante" OR "anti-migrantes")))) OR


<<<Salud>>>
(enmiend* NEAR/3f
((libertad NEAR/1f elección) OR (eleccion NEAR/1f salud) OR isapre* OR ((plan NEAR/0f unico) NEAR/0f universal) OR (propuesta NEAR/1f salud))) OR

<<<Pensiones>>>
(enmiend* NEAR/3f
(pension* OR afp OR (papi* NEAR/0f corazon) OR (((con NEAR/1f mi) NEAR/0f plata) NEAR/0f no))) OR

<<<Seguridad>>>
(enmiend* NEAR/3f
((fuerza* NEAR/0f (armada* OR especial*)) OR ffaa OR "ff.aa" OR  (policia NEAR/0f fronteriza) OR (prote* NEAR/2f fronter*) OR carabiner* OR (justicia NEAR/0f militar) OR ((fuerza* NEAR/0f especial*) NEAR/0f fronter*))) OR

<<<Personas de interés>>>
((Luis NEAR/0f Silva) OR (profe NEAR/0f silva) OR @profesor_silva OR
(Yerko NEAR/0f Ljubetic) OR @YerkoLjubetic OR
(Beatriz NEAR/0f Hevia) OR (Bea NEAR/0f hevia) OR @beaheviaw OR
(Alexis NEAR/0f Cortés) OR @AlexisCortesMs OR
(María NEAR/0f Pardo) OR @mariapardover OR
(María NEAR/0f Gatica) OR (la NEAR/0f gatica) OR
(Mariela NEAR/0f Fincheira) OR @Marielaandreafm)
''', 
"Mujer Migrante y Violencia Politica Genero en Colombia": """
<<<Referencia a venezolanos>>>
(
(veneca* OR ((Invasora* OR aprovechada* OR malandra* OR usurpadora* OR embarazada* OR asesina* OR prostituta* OR ((roba OR quita) NEAR/2F marido*) OR puta* OR perra OR muchachita* OR recogida* OR buscona* OR mamadora* OR cansona* OR parturienta* OR ratera* OR hampona* OR ampona*) NEAR/7F (veneca* OR extranjera* OR venezolana* OR (mujer* NEAR/3F vene*))) OR
((oleada* OR bus*) NEAR/1 (veneca* OR extranjera* OR 
venezolana*))) OR
((mujer* OR niña* OR señora* OR niñita* OR chama* OR "la man" OR culicagada* OR hermana*) NEAR/7F (veneca* OR migrante* OR venezuela* OR venezolana* OR extranjera*)) OR "mujer venezolana"

OR

<<<Migración ilegal y desplazamiento>>>
(author:(migracioncol OR IvanDuque OR petrogustavo OR MigracionesPe OR rlopezaliaga1 OR dsalaverryv OR HDeSotoPeru OR OIM_Peru) AND (
(veneca* OR venezolana* OR ((Invasora* OR aprovechada* OR malandra* OR usurpadora*) NEAR/7 (veneca* OR extranjera* OR venezolana*)) OR
(oleada* NEAR/1 (veneca* OR extranjera* OR venezolana*)))
))

OR 

((@migracioncol OR @IvanDuque OR duque OR petro OR @petrogustavo OR (colombia NEAR/1 huamana) OR @MigracionesPe OR @OIM_Peru OR @rlopezaliaga1 OR @dsalaverryv OR @HDeSotoPeru OR salaverry) NEAR/7 ((veneca* OR Invasora* OR venezolana* OR aprovechada* OR malandra* OR usurpadora*) OR (oleada* NEAR/1 (veneca* OR extranjera*))) 
)

OR
#NoMasVenezolanasEnColombia OR #DeportenlasYa
)
<<<LO QUE NO NOS INTERESA>>>
NOT
(
<<<Contenido sexual>>>
url: www.denunciando.com OR
<<<Contenido Político>>>
(financi* NEAR/1 campaña) OR (director* NEAR/1 (centro NEAR/1 democratico)) OR dictadura OR ((en OR ira OR compatriota* OR estudiar OR rid?culo OR patrimonio OR cargo* OR desde OR "en el" OR vista OR votar OR financia* OR conocer ) NEAR/6 (extranjero)) OR
((oposicion OR gobierno OR dictadura) NEAR/1 (venezolan* OR venezuela)) OR d OR turquia OR narcoterroris* OR (narco NEAR/1f (terroris* OR chavis* OR dictadura)) OR maduro OR guaido OR 16J OR tortura OR "libertad al pueblo venezolano" OR (asamblea NEAR/1f nacional) OR (diputad* NEAR/1 venezolan*) OR constituyente OR (preso* NEAR/1f politico*) OR tirano OR regimen OR chavis* OR sajarov OR farc OR petro OR chavez OR chaves OR jolie OR odebrecht OR #rusia2018 OR narcotrafico OR fidel OR castrochavis* OR (papa NEAR/1f francisco) OR nairo OR bolivar OR trump OR expropia* OR (eleccion* NEAR/1 libre*) OR (cese NEAR/1 usuarpacion) OR (grupo NEAR/1 lima) OR (gobierno NEAR/1 transicion) OR ((opositor* OR oposicion*) NEAR/1 (venezolan* OR venezuela)) OR (alejandro NEAR/1 guerra) OR ((lobo OR lobito) NEAR/1 guerra) OR ((estado OR gobierno) NEAR/1 (venezolan* OR venezuela)) OR (usurpacion NEAR/1 (venezolana OR venezuela OR gobierno)) OR (malandr* NEAR/2 (petro OR izquierd*)) OR

(Peru NEAR/10 contagio) OR (socialismo NEAR/10 venezolano) OR
(medicos NEAR/10 cubanos) OR
(@jguaido NEAR/3 oposicion) OR
(guerrilleros NEAR/20 virus) OR
(Coalicion NEAR/20 cubanos) OR
(Vacuna NEAR/1 Rusa) OR
(( Peru NEAR/10 contagio)OR(socialismo NEAR/10 venezolano)OR(medicos NEAR/10 cubanos)) OR
(darles NEAR/9 necesitadas) OR
(ganas NEAR/8 directo) OR
(venequita) OR
(victoria NEAR/4 venezuela) OR
(Lauderdale) OR
(incauta* NEAR/3 rifles) OR
(Ayala NEAR/10 democracia) OR
(campaña NEAR/10 300) OR
(trinidad NEAR/1 tobago) OR
(congo) OR
( (1.800 OR 1800) NEAR/3 millones) OR
(consulado NEAR/3 saqueado) OR
(red NEAR/5 trafico) OR
(asesinada NEAR/5 EEUU) OR
(Aruba NEAR/5 delincuentes) OR



<<<Variedad o shit chat>>>

"Dua Lipa" OR
(año NEAR/1f nuevo) OR pernil OR
(ñeñe) OR
(jorge NEAR/1 alfaro) OR
(gasolina NEAR/5 enfrentamiento*) OR
(450 NEAR/5 sanear) OR
(sucursal NEAR/3 mercantil) OR fanb OR pdvsa OR ((soberanía OR beisbol OR economia OR moneda OR petroleo OR petroler* OR futbol* OR equipo OR "segunda division" OR playa OR seleccion OR rock OR musica OR emisora* OR periodista* OR constitucion OR actor OR iglesia* OR portal OR modelo OR andes OR prensa OR actriz OR crudo OR delantero) NEAR/2 (venezuel* OR venezolan*)))

OR
<<<Violencia Politica Genero>>>
((ingrid NEAR/1 betancur) OR (paola NEAR/1f holguin) OR (margarita NEAR/1f rastrepo) OR (caterine NEAR/1f ibarguen) OR (ana NEAR/1f agudelo) OR (Elizabeth NEAR/1f giraldo) OR (francia NEAR/1f marquez) OR (piedad NEAR/1f cordoba) OR (martha NEAR/1f peralta) OR (isabel NEAR/1f zuleta) OR (susana NEAR/1f boreal) OR (andrea NEAR/1f padilla) OR (sara NEAR/1f castellanos) OR (clara NEAR/1f sandoval) OR ((juana OR juanita) NEAR/1f castaño) OR ((juana OR juanita) NEAR/1f goebertus) OR
@IBetancourtCol OR @MabelLaraNews OR @tripleCIbarguen OR @AnaPaolaAgudelo OR @laclasemediera OR @FranciaMarquezM OR (sandra NEAR/1f borda) OR @sandraborda OR (paloma  NEAR/1f Valencia) OR @PalomaValenciaL OR (maria NEAR/1f (fernanda NEAR/1 Cabal)) OR @MariaFdaCabal OR (Maria NEAR/1 Pizarro) OR @PizarroMariaJo OR (angelica NEAR/1f lozano) OR @AngelicaLozanoC OR (Cathy NEAR/1 Juvinao) OR @CathyJuvinao OR (maria NEAR/2f Carrascal) OR @MafeCarrascal OR @JuanitaGoe OR (katherine NEAR/1f Miranda) OR @MirandaBogota OR @PaolaHolguin OR @MargaritaRepo OR @piedadcordoba OR @marthaperaltae OR @ISAZULETA OR @SusanaBoreal OR @andreanimalidad OR @sarag12 OR @clarasandoval OR @juanitacatano OR @VenecaGang_ OR author: VenecaGang_)
"""
}