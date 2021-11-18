from .dataclass import host_index as _host_index, stats_index as _stats_index


prefs_indexes = (  # by Koupah and Vresod,
	"lastPlayerName",
	"touchConfig",
	"colorConfig",
	"unused3",
	"unused4",
	"unused5",
	"unused6",
	"unused7",
	"ShowMinPlayerWarning",
	"showOnlineHelp",
	"lastHat",
	"sfxVolume",
	"musicVolume",
	"joyStickSize",
	"lastGameStart",
	"lastSkin",
	"lastPet",
	"censorChat",
	"lastLanguage",
	"vsync",
	"showAdsScreen2",
	"privacyPolicyVersion",
	"unused22",
	"birthDateMonth",
	"birthDateDay",
	"birthDateYear",
	"birthDateSetDate",
	"chatModeType",
	"isGuest",
	"guardianEmail",
	"hasLoggedin",
	"accountLoginStatus",
	"lastSchemaVersion",
	"lastVisor",
	"lastNameplate",
	"playerLevel",
	"playerXp",
	"lastCosmicube",
	"crossplayAllPlatforms",
	"playerXpRequiredForNextLevel",
	"enableMouseMovement",
	"askRedeemDLC",
	"warnedAboutGuestModeProgression",
)

host_indexes = (
	_host_index('version','byte',1),
	_host_index('MaxPlayers','byte',1),
	_host_index('Keywords','uint32',4),
	_host_index('MapId','byte',1),
	_host_index('PlayerSpeedMod','single',4),
	_host_index('CrewLightMod','single',4),
	_host_index('ImposterLightMod','single',4),
	_host_index('KillCooldown','single',4),
	_host_index('NumCommonTasks','byte',1),
	_host_index('NumLongTasks','byte',1),
	_host_index('NumShortTasks','byte',1),
	_host_index('NumEmergencyMeetings','int32',4),
	_host_index('NumImposters','byte',1),
	_host_index('KillDistance','byte',1),
	_host_index('DiscussionTIme','int32',4),
	_host_index('VotingTime','int32',4),
	_host_index('isDefaults','boolean',1),
	_host_index('EmergencyCooldown','byte',1),
	_host_index('ConfirmImposter','boolean',1),
	_host_index('VisualTasks','boolean',1),
	_host_index('AnonymousVotes','boolean',1),
	_host_index('TaskBarMode','byte',1),
)

stats_indexes = ( # by EnbyCosmog
	_stats_index('version','byte',1),
	_stats_index('BodiesReported','uint32',4),
	_stats_index('EmergenciesCalled','uint32',4),
	_stats_index('TasksCompleted','uint32',4),
	_stats_index('AllTasksCompleted','uint32',4),
	_stats_index('SabotagesFixed','uint32',4),
	_stats_index('ImposterKills','uint32',4),
	_stats_index('TimesMurdered','uint32',4),
	_stats_index('TimesEjected','uint32',4),
	_stats_index('CrewmateStreak','uint32',4),
	_stats_index('TimesImposter','uint32',4),
	_stats_index('TimesCrewmate','uint32',4),
	_stats_index('GamesStarted','uint32',4),
	_stats_index('GamesFinished','uint32',4),
	_stats_index('CrewmateVoteWins','uint32',4),
	_stats_index('CrewmateTaskWins','uint32',4),
	_stats_index('ImposterVoteWins','uint32',4),
	_stats_index('ImposterKillWins','uint32',4),
	_stats_index('ImposterSabotageWins','uint32',4),
)

hats_dict = { # by EnbyCosmog (this took so long ;-;). special thanks to SharedLines for providing the initial version of this list
	'': 'None',
	'hat_NoHat': 'None',
	'hat_bushhat': 'Done D', 
	'hat_captain': 'Cap-tain', 
	'hat_doubletophat': 'Toppat Chief', 
	'hat_flowerpot': 'Planted', 
	'hat_military': 'Militant', 
	'hat_MilitaryWinter': 'Militant - Winter', 
	'hat_GovtDesert': 'Militant - Desert', 
	'hat_police': 'Militant - Police', 
	'hat_Rupert': 'Rupert', 
	'hat_partyhat': 'P Hat', 
	'hat_tophat': 'Toppat Grunt', 
	'hat_towelwizard': 'Freshly Showered', 
	'hat_russian': 'Wall Ushanka', 
	'hat_viking': 'Vi King', 
	'hat_wallcap': 'The Wall Cap', 
	'hat_pk06_Snowman': 'Frosted', 
	'hat_pk06_Reindeer': 'Oh Dear, Rain', 
	'hat_pk06_Lights': 'Lit Up', 
	'hat_pk06_Santa': 'Presents Dude', 
	'hat_pk06_tree': 'Evergreen', 
	'hat_pk06_Present': 'Gift Wrapped', 
	'hat_pk06_Candycanes': "Can'tdy Cane", 
	'hat_pk06_ElfHat': 'Toy Dude', 
	'hats_newyears2018': 'New Years 2019', 
	'hat_whitetophat': 'Toppat White Edition', 
	'hat_pk02_Crown': 'Crowned', 
	'hat_pk02_Eyebrows': 'Stickmin Brows', 
	'hat_pk02_HaloHat': 'Innocence', 
	'hat_pk02_PipCap': 'Tiny Jim', 
	'hat_pk02_ScubaHat': 'Aquatic Apparatus', 
	'hat_pk02_StickminHat': 'Stickmin Rider', 
	'hat_pk02_StrawHat': 'Serengetti Outta Here', 
	'hat_pk02_ThirdEyeHat': 'Third Eye', 
	'hat_pk02_ToiletPaperHat': 'The Last Wipe', 
	'hat_pk02_Toppat': 'The New Chief', 
	'hat_pk03_Fedora': 'Fedorable', 
	'hat_pk03_StrapHat': 'Gartner', 
	'hat_pk04_Banana': 'Peeled', 
	'hat_pk04_Bear': 'Unbearable', 
	'hat_pk05_Cheese': 'Bein Cheesy', 
	'hat_pk05_Cherry': 'Cherry On Top', 
	'hat_pk05_Egg': 'Eggscellent', 
	'hat_pk05_Fedora': 'Noire Evening', 
	'hat_pk05_Flamingo': 'Floaty Flamingo', 
	'hat_pk05_FlowerPin': "Daisy Me Rollin'", 
	'hat_pk05_Helmet': 'Knighted', 
	'hat_pk05_Plant': 'Young Sprout', 
	'hat_pkHW01_PlagueHat': 'Plagued', 
	'hat_pkHW01_Pumpkin': 'Punkin', 
	'hat_pkHW01_Pirate': 'Walk The Plank', 
	'hat_pkHW01_Machete': 'Chop-Chop', 
	'hat_pk04_Archae': 'Siberia James', 
	'hat_pk04_Balloon': 'We All Float Here', 
	'hat_pk04_BirdNest': 'Two Eggs in a Nest', 
	'hat_pk04_Chef': 'My Name Chef', 
	'hat_pk04_CCC': 'C4', 
	'hat_pk04_Fez': 'Fez Up', 
	'hat_pk04_GeneralHat': 'Generally Speaking', 
	'hat_pk04_Pompadour': 'Pompous Pompadour', 
	'hat_pk04_HunterCap': 'Nimrod', 
	'hat_pk04_JungleHat': 'Take Cover', 
	'hat_WinterHelmet': 'Take Cover - Winter', 
	'hat_pk04_MiniCrewmate': 'Mini Crewmate', 
	'hat_pk04_Vagabond': 'Mysterious Vagabond', 
	'hat_pk04_Snowman': 'Snowmate', 
	'hat_pk05_davehat': 'Museum Scurity', 
	'hat_pk05_Ellie': 'Redd-Headed Outlaw', 
	'hat_pk05_Svenhat': 'Sven Svensson', 
	'hat_pk05_Burthat': "I'm Burt", 
	'hat_pk05_Ellryhat': 'Funky Fusion', 
	'hat_pk05_Wizardhat': 'A Real Wiz', 
	'hat_pk05_cheesetoppat': 'Muenster', 
	'hat_pk05_Macbethhat': 'Mr. Macbeth', 
	'hat_pk05_HenryToppat': 'Recruited Henry', 
	'hat_pk05_EllieToppat': 'Recruited Ellie', 
	'hat_pk05_GeoffreyToppat': 'Bighead', 
	'hat_Chocolate': 'Chocolate Scoop', 
	'hat_Heart': 'I Heart U', 
	'hat_Ponytail': 'Blondie', 
	'hat_Rubberglove': 'You Glove To See It', 
	'hat_Unicorn': "Magical 'Corn", 
	'hat_Zipper': 'Crewmate Suit', 
	'hat_CuppaJoe': 'Surveillance Joe', 
	'hat_HardtopHat': 'Crane Operator', 
	'hat_Prototype': 'Prototype Helmet', 
	'hat_Records': 'Records Recorder', 
	'hat_ThomasC': 'Thomas Top', 
	'hat_ToppatHair': 'Cool Katie', 
	'hat_WilfordIV': 'Sir Wilford IV', 
	'hat_Winston': 'Corrupted Official', 
	'hat_AbominalHat': 'Abominal Head', 
	'hat_EarnmuffBlue': 'Muffs For The Ears', 
	'hat_EarmuffGreen': 'Muffs For The Ears - Green', 
	'hat_EarmuffsPink': 'Muffs For The Ears - Pink', 
	'hat_EarmuffsYellow': 'Muffs For The Ears - Yellow', 
	'hat_pk04_MinerCap': 'Miner Setback', 
	'hat_MinerBlack': 'Miner Setback - Black', 
	'hat_MinerYellow': 'Miner Setback - Yellow', 
	'hat_RockIce': 'Ice Cap', 
	'hat_RockLava': 'Eruptive', 
	'hat_SnowbeanieRed': 'Winter Arrives', 
	'hat_SnowbeanieGreen': 'Winter Arrives - Green', 
	'hat_SnowbeanieOrange': 'Winter Arrives - Orange', 
	'hat_SnowBeaniePurple': 'Winter Arrives - Purple', 
	'hat_pk04_WinterHat': 'Cold One', 
	'hat_WinterGreen': 'Cold One - Green', 
	'hat_WinterRed': 'Cold One - Red', 
	'hat_WinterYellow': 'Cold One - Yellow', 
	'hat_Voleyball': 'Spiked', 
	'hat_Basketball': 'Hole in One', 
	'hat_Bowlingball': 'Strike', 
	'hat_Deitied': 'Shrine to the Deities', 
	'hat_Dodgeball': "You're Out!", 
	'hat_DrillMetal': 'Drill', 
	'hat_DrillStone': 'Drill - Stone', 
	'hat_DrillWood': 'Drill - Wood', 
	'hat_Janitor': 'Haunted Hotel Hat', 
	'hat_Pot': 'Digging Helmet', 
	'hat_Soccer': 'Header', 
	'hat_Visor': 'Visor Hat', 
	'hat_mira_bush': 'One in the Hand', 
	'hat_mira_case': 'Important Documents', 
	'hat_mira_cloud': 'Head in the Clouds', 
	'hat_mira_flower': 'Exotic Flower', 
	'hat_mira_flower_red': 'Exotic Flower - Red', 
	'hat_mira_gem': 'Unique Specimen', 
	'hat_pk03_Headphones': 'Greatest Headset', 
	'hat_GovtHeadset': 'Greatest Headset - Green', 
	'hat_mira_headset_blue': 'Greatest Headset - Blue', 
	'hat_mira_headset_pink': 'Greatest Headset - Pink', 
	'hat_mira_headset_yellow': 'Greatest Headset - Yellow', 
	'hat_mira_leaf': 'Vine Just Vine', 
	'hat_mira_milk': 'Peach Drink', 
	'hat_pk04_Slippery': 'Slippery When Wet', 
	'hat_mira_sign_blue': 'Slippery When Wet - Blue', 
	'hat_pk03_Security1': 'Tightened Security', 
	'hat_pk04_Antenna': 'Poor Reception', 
	'hat_Antenna_Black': 'Poor Reception - Black', 
	'hat_astronaut': 'Spacewalk', 
	'hat_Astronaut-Blue': 'Spacewalk - Blue', 
	'hat_Astronaut-Cyan': 'Spacewalk - Light Blue', 
	'hat_Astronaut-Orange': 'Spacewalk - Orange', 
	'hat_pk04_Bandana': 'Greh', 
	'hat_Bandana_Blue': 'Greh - Blue', 
	'hat_Bandana_Green': 'Greh - Green', 
	'hat_Bandana_Pink': 'Greh - Pink', 
	'hat_Bandana_Red': 'Greh - Red', 
	'hat_Bandana_White': 'Greh - White', 
	'hat_Bandana_Yellow': 'Greh - Yellow', 
	'hat_pk01_BaseballCap': "The Ol' Ball Game", 
	'hat_baseball_Black': "The Ol' Ball Game - Black", 
	'hat_baseball_Green': "The Ol' Ball Game - Green", 
	'hat_baseball_Lightblue': "The Ol' Ball Game - Light Blue", 
	'hat_baseball_LightGreen': "The Ol' Ball Game - Light Green", 
	'hat_baseball_Lilac': "The Ol' Ball Game - Lilac", 
	'hat_baseball_Orange': "The Ol' Ball Game - Orange", 
	'hat_baseball_Pink': "The Ol' Ball Game - Pink", 
	'hat_baseball_Purple': "The Ol' Ball Game - Purple", 
	'hat_baseball_Red': "The Ol' Ball Game - Red", 
	'hat_baseball_White': "The Ol' Ball Game - White", 
	'hat_baseball_Yellow': "The Ol' Ball Game - Yellow", 
	'hat_pk04_Beanie': 'Beanie', 
	'hat_Beanie_Black': 'Beanie - Black', 
	'hat_Beanie_Blue': 'Beanie - Blue', 
	'hat_Beanie_Green': 'Beanie - Green', 
	'hat_Beanie_Lightblue': 'Beanie - Baby Blue', 
	'hat_Beanie_LightGreen': 'Beanie - Baby Green', 
	'hat_Beanie_LightPurple': 'Beanie - Baby Pink', 
	'hat_Beanie_Pink': 'Beanie - Pink', 
	'hat_Beanie_Purple': 'Beanie - Purple', 
	'hat_Beanie_White': 'Beanie - White', 
	'hat_Beanie_Yellow': 'Beanie - Yellow', 
	'hat_stethescope': 'What Is Up, Doc?', 
	'hat_Doc_black': 'What Is Up, Doc? - Black', 
	'hat_Doc_Orange': 'What Is Up, Doc? - Orange', 
	'hat_Doc_Purple': 'What Is Up, Doc? - Purple', 
	'hat_Doc_Red': 'What Is Up, Doc? - Red', 
	'hat_Doc_White': 'What Is Up, Doc? - White', 
	'hat_pk04_DoRag': 'Swarshburgalor', 
	'hat_Dorag_Black': 'Swarshburgalor - Coal', 
	'hat_Dorag_Desert': 'Swarshburgalor - Desert', 
	'hat_Dorag_Jungle': 'Swarshburgalor - Woodland', 
	'hat_Dorag_Purple': 'Swarshburgalor - Purple', 
	'hat_Dorag_Sky': 'Swarshburgalor - Sky', 
	'hat_Dorag_Snow': 'Swarshburgalor - Snow', 
	'hat_Dorag_Yellow': 'Swarshburgalor - Citrus', 
	'hat_pk03_Goggles': 'Safety Second', 
	'hat_goggles': 'Goggles Up', 
	'hat_Goggles_Black': 'They Do Nothing - Black', 
	'hat_Goggles_Chrome': 'They Do Nothing - Chrome', 
	'hat_hardhat': 'Ohsa Compliant', 
	'hat_Hardhat_black': 'Ohsa Compliant - Black', 
	'hat_Hardhat_Blue': 'Ohsa Compliant - Blue', 
	'hat_Hardhat_Green': 'Ohsa Compliant - Green', 
	'hat_Hardhat_Orange': 'Ohsa Compliant - Orange', 
	'hat_Hardhat_Pink': 'Ohsa Compliant - Pink', 
	'hat_Hardhat_Purple': 'Ohsa Compliant - Purple', 
	'hat_Hardhat_Red': 'Ohsa Compliant - Red', 
	'hat_Hardhat_White': 'Ohsa Compliant - White', 
	'hat_brainslug': 'Headslug', 
	'hat_headslug_Purple': 'Hadslug - Purple', 
	'hat_headslug_Red': 'Headslug - Red', 
	'hat_headslug_Yellow': 'Headslug - Yellow', 
	'hat_headslug_White': 'Headslug - White', 
	'hat_pk02_HeroCap': 'Hooded Figure', 
	'hat_Herohood_Black': 'Hooded Figure - Black', 
	'hat_Herohood_Blue': 'Hooded Figure - Blue', 
	'hat_Herohood_Pink': 'Hooded Figure - Pink', 
	'hat_Herohood_Purple': 'Hooded Figure - Purple', 
	'hat_Herohood_Red': 'Hooded Figure - Red', 
	'hat_Herohood_White': 'Hooded Figure - White', 
	'hat_Herohood_Yellow': 'Hooded Figure - Yellow', 
	'hat_paperhat': 'Folded', 
	'hat_Paperhat_Black': 'Folded - Black', 
	'hat_Paperhat_Blue': 'Folded - Blue', 
	'hat_Paperhat_Cyan': 'Folded - Seafoam', 
	'hat_Paperhat_Lightblue': 'Folded - Sky', 
	'hat_Paperhat_Pink': 'Folded - Pink', 
	'hat_Paperhat_Yellow': 'Folded - Yellow', 
	'hat_pk02_PlungerHat': 'Clogged', 
	'hat_Plunger_Blue': 'Clogged - Blue', 
	'hat_Plunger_Yellow': 'Clogged - Black N Yellow ', 
	'hat_pk04_RamHorns': 'Rammed', 
	'hat_Ramhorn_Black': 'Rammed - Black', 
	'hat_Ramhorn_Red': 'Rammed - Red', 
	'hat_Ramhorn_White': 'Rammed - White', 
	'hat_pk02_TenGallonHat': 'Ten Gallons', 
	'hat_TenGallon_Black': 'Ten Gallons - Black', 
	'hat_TenGallon_White': 'Ten Gallons - White', 
	'hat_pk03_Traffic': 'Traffic Jam', 
	'hat_Traffic_Blue': 'Traffic Jam - Blue', 
	'hat_Traffic_Red': 'Traffic Jam - Red', 
	'hat_Traffic_Yellow': 'Traffic Jam - Yellow', 
	'hat_traffic_purple': 'Traffic Jam - Purple',  
	'hat_arrowhead': "Arrow'd", 
	'hat_axe': 'Splitting Headache', 
	'hat_pkHW01_ScaryBag': 'Mask, The Monster Mask', 
	'hat_papermask': 'Mask, The Monster Mask - Light',
	'hat_pkHW01_BatWings': 'Batty', 
	'hat_bat_crewcolor': 'Batty - Crewcolor', 
	'hat_bat_green': 'Batty - Green',
	'hat_bat_ice': 'Batty - Ice',
	'hat_bone': "You're Boned", 
	'hat_candycorn': 'Candycorny', 
	'hat_pkHW01_CatEyes': 'Batbean', 
	'hat_cat_grey': 'Batbean - Grey', 
	'hat_cat_orange': 'Batbean - Orange', 
	'hat_cat_pink': 'Batbean - Pink', 
	'hat_cat_snow': 'Batbean - Snow', 
	'hat_clown_purple': 'Clown Town', 
	'hat_pkHW01_Horns': 'Imp-ressive', 
	'hat_devilhorns_crewcolor': 'Imp-pressve - Crewcolor', 
	'hat_devilhorns_green': 'Imp-pressve - Green', 
	'hat_devilhorns_murky': 'Imp-pressve - Murky', 
	'hat_devilhorns_white': 'Imp-pressve - White', 
	'hat_devilhorns_black': 'Imp-pressve - Black', 
	'hat_devilhorns_yellow': 'Imp-ressive - Gold',
	'hat_fairywings': 'Fairy Flutters', 
	'hat_fishhed': 'Fish Hed', 
	'hat_frankenbolts': 'Frankenbolts', 
	'hat_frankenbride': "Franken's Spouse", 
	'hat_glowstick': 'Up All Night Raving', 
	'hat_pkHW01_Mohawk': 'Morawk', 
	'hat_mohawk_bubblegum': 'Morawk - Bubblegum', 
	'hat_mohawk_bumblebee': 'Morawk - Bumblebee', 
	'hat_mohawk_purple_green': 'Morawk - Purplegreen', 
	'hat_mohawk_rainbow': 'Morawk - Rainbow', 
	'hat_mummy': 'Mummy Mood', 
	'hat_tombstone': 'RIP in Pieces', 
	'hat_pkHW01_Witch': 'Witch One', 
	'hat_witch_green': 'Witch One - Green', 
	'hat_witch_murky': 'Witch One - Murky', 
	'hat_witch_pink': 'Witch One - Pink', 
	'hat_witch_white': 'Witch One - White', 
	'hat_pkHW01_Wolf': 'Wearwolf', 
	'hat_wolf_murky': 'Wearwolf - Murky', 
	'hat_wolf_grey': 'Wearwolf - Grey', 
	'hat_vi': "Vi's Hair", 
	'hat_caitlin': "Caitlyn's Cap", 
	'hat_clagger': "Claggor's Goggles", 
	'hat_comper': 'Chomper', 
	'hat_enforcer': 'Enforcer Helmet', 
	'hat_heim': "Heimerdinger's Hair", 
	'hat_jayce': "Jayce's Hair", 
	'hat_jinx': "Jinx's Hair"
}

skins_dict = { # by EnbyCosmog. special thanks to SharedLines for providing the initial version of this list
	'': 'None',
	'skin_None': 'None', 
	'skin_Capt': "Pilot's License", 
	'skin_Police': 'Policeman Officer', 
	'skin_Wall': 'Guarding the Wall', 
	'skin_Security': 'Keepin it Secure', 
	'skin_Tarmac': 'Land Here', 
	'skin_Archae': 'Unearthed Wonders', 
	'skin_CCC': 'Chaos Containment Crewmate', 
	'skin_rhm': 'Right Hand Man: Reborn', 
	'skin_Bling': 'Bling Bling', 
	'skin_General': 'General Galeforce', 
	'skin_Mech': "I'll Fix it", 
	'skin_MechanicRed': 'Airship Mechanic', 
	'skin_Military': 'Officer Outfit', 
	'skin_MilitaryDesert': 'Officer - Desert', 
	'skin_MilitarySnowskin': 'Officer - Snow', 
	'skin_prisoner': 'Inmate 2112', 
	'skin_PrisonerBlue': 'Inmate 2112 - Blue', 
	'skin_PrisonerTanskin': 'Inmate 2112 - Tan', 
	'skin_SuitB': 'Suited up', 
	'skin_SuitW': 'Flashy', 
	'skin_Skin_SuitRedskin': 'Toppat Uniform', 
	'skin_ToppatSuitFem': 'Toppat Skirt', 
	'skin_ToppatVest': 'Vested Interest', 
	'skin_Winter': 'Jacket up', 
	'skin_JacketGreenskin': 'Jacket up - Green', 
	'skin_JacketPurpleskin': 'Jacket up - Purple', 
	'skin_JacketYellowskin': 'Jacket up - Yellow', 
	'skin_Abominalskin': 'Abominal Snowmate', 
	'skin_Miner': 'Underminer', 
	'skin_MinerBlackskin': 'Underminer - Black', 
	'skin_RockIceskin': 'Ice to Meet You', 
	'skin_RockLavaskin': 'Rock Solid', 
	'skin_Sweaterskin': 'Cozy Sweater', 
	'skin_SweaterBlueskin': 'Cozy Sweater - Blue', 
	'skin_SweaterPinkskin': 'Cozy Sweater - Pink', 
	'skin_SweaterYellowskin': 'Cozy Sweater - Yellow', 
	'skin_SportsRedskin': 'Sports Team Red', 
	'skin_SportsBlueskin': 'Sports Team Blue', 
	'skin_D2Cskin': 'Digging Kid', 
	'skin_Janitorskin': 'Janitorial Duties', 
	'skin_Bushskin': 'Sneaky', 
	'skin_BusinessFemskin': 'Business Skirt', 
	'skin_BusinessFem-Aquaskin': 'Business Skirt - Aqua', 
	'skin_BusinessFem-Tanskin': 'Business Skirt - Tan', 
	'skin_Hazmat': 'Hazmate', 
	'skin_Hazmat-Blackskin': 'Hazmate - Black',
	'skin_Hazmat-Blueskin': 'Hazmate - Blue',
	'skin_Hazmat-Greenskin': 'Hazmate - Green',
	'skin_Hazmat-Pinkskin': 'Hazmate - Pink',
	'skin_Hazmat-Redskin': 'Hazmate - Red',
	'skin_Hazmat-Whiteskin': 'Hazmate - White',
	'skin_Astro': 'Astronaught',
	'skin_Astronaut-Blueskin': 'Astronaut - Blueskin',
	'skin_Astronaut-Cyanskin': 'Astronaut - Cyanskin',
	'skin_Astronaut-Orangeskin': 'Astronaut - Orangeskin',
	'skin_Science': 'Scientific Theory',
	'skin_Scientist-Blueskin': 'Doctor',
	'skin_Scientist-Darkskin': 'Dark Scientist',
	'skin_clown': 'Crewbo the Clown',
	'skin_fairy': 'Fairy Godcrewmate',
	'skin_fishmonger': 'The Fishmonger',
	'skin_mummy': 'I Want my Mummy',
	'skin_pumpkin': "Big Ol' Pumpkin Pants",
	'skin_vampire': 'I Vant to Keel',
	'skin_witch': 'Whimsy Witch',
	'skin_caitlin': "Caitlyn's Uniform",
	'skin_enforcer': 'Enforcer Armor',
	'skin_heim': "Heimerdinger's Suit",
	'skin_jayce': "Jayce's Council Suit",
	'skin_jinx': "Jinx's Clothes",
	'skin_vi': "Vi's Clothes"
}

visors_dict = { # by EnbyCosmog. special thanks to SharedLines for providing the initial version of this list
	'': 'None',
	'visor_EmptyVisor': 'None', 
	'visor_pk01_FredVisor': 'Great Goalie', 
	'hat_geoff': 'My Name Geoff', 
	'visor_pk01_MonoclesVisor': 'Double Monocles', 
	'visor_pk01_PaperMaskVisor': 'Safe Not Sorry', 
	'visor_pk01_PlagueVisor': 'Plauged', 
	'visor_pk01_RHMVisor': 'Right Hand Stache', 
	'visor_pk01_Security1Visor': 'Shades', 
	'visor_pk01_AngeryVisor': 'A N G E R Y', 
	'visor_BillyG': 'Mr. G', 
	'visor_Galeforce': 'Galeforce Whiskers', 
	'visor_Krieghaus': 'Krieghaus', 
	'visor_Reginald': 'Reginald Stache', 
	'visor_Scar': 'Scarred', 
	'visor_WinstonStache': 'Riding Shotgun', 
	'visor_Lava': 'Helmelted', 
	'visor_polus_ice': 'Icicle Tears', 
	'visor_SkiGogglesWhite': 'Hit the Slopes', 
	'visor_SkiGoggleBlack': 'Hit the Slopes - Black', 
	'visor_SKiGogglesOrange': 'Hit the Slopes - Orange', 
	'visor_shopglasses': 'Shop Here', 
	'visor_D2CGoggles': 'Dig Down', 
	'visor_is_beard': 'A Beard', 
	'visor_JanitorStache': 'Ghostly Moustache', 
	'visor_Mouth': 'Wurm', 
	'visor_mira_card_blue': 'Passcard - Blue', 
	'visor_mira_card_red': 'Passcard - Red', 
	'visor_mira_glasses': 'Spectacles', 
	'visor_pk01_HazmatVisor': 'Blocks Toxics', 
	'visor_mira_mask_black': 'Blocks Toxics - Black', 
	'visor_mira_mask_blue': 'Blocks Toxics - Blue', 
	'visor_mira_mask_green': 'Blocks Toxics - Green', 
	'visor_mira_mask_purple': 'Blocks Toxics - Purple', 
	'visor_mira_mask_red': 'Blocks Toxics - Red', 
	'visor_mira_mask_white': 'Blocks Toxics - White', 
	'visor_pk01_DumStickerVisor': 'Note 2 Self', 
	'visor_Stickynote_Cyan': 'Note 2 Self - Cyan', 
	'visor_Stickynote_Green': 'Note 2 Self - Green', 
	'visor_Stickynote_Orange': 'Note 2 Self - Orange', 
	'visor_Stickynote_Pink': 'Note 2 Self - Pink', 
	'visor_Stickynote_Purple': 'Note 2 Self - Purple', 
	'visor_Blush': 'Oh You', 'visor_Bomba': 'Bombastic', 
	'visor_Carrot': 'Happeh', 
	'visor_Crack': 'Among Us Cracked 2021', 
	'visor_Dirty': 'Wash Me', 
	'visor_Dotdot': 'Dot Dot Dot', 
	'visor_EyepatchL': 'Patched Eye - Left', 
	'visor_EyepatchR': 'Patched Eye - Right', 
	'visor_LolliBlue': 'Lollipop - Blue', 
	'visor_LolliBrown': 'Lollipop - Brown', 
	'visor_LolliOrange': 'Lollipop - Orange', 
	'visor_LolliRed': 'Lollipop', 
	'visor_PiercingL': 'Pierced - Left', 
	'visor_PiercingR': 'Pierced - Right', 
	'visor_SciGoggles': 'Safety First', 
	'visor_SmallGlasses': 'Tiny Specs', 
	'visor_SmallGlassesBlue': 'Tiny Specs - Blue', 
	'visor_SmallGlassesRed': 'Tiny Specs - Red', 
	'visor_Straw': 'Dadgum', 
	'visor_eyeball': 'Got My Eye On You', 
	'visor_clownnose': "Clownin' Around", 
	'visor_masque_blue': "Masque'd Up - Blue", 
	'visor_masque_green': "Masque'd Up - Green", 
	'visor_masque_red': "Masque'd Up - Red", 
	'visor_masque_white': "Masque'd Up - White", 
	'visor_mummy': "That's a Wrap", 
	'visor_heim': "Heimerdinger's Moustache", 
	'visor_jinx': "Jinx's Goggles"
}

nameplates_dict = { # by Enby Cosmog
	'': 'None',
	'nameplate_NoPlate': 'None', 
	'nameplate_airship_Toppat': 'Airship Toppat', 
	'nameplate_airship_CCC': 'C4 Plate', 
	'nameplate_airship_Diamond': 'Diamonds!', 
	'nameplate_airship_Emerald': 'Emeralds!', 
	'nameplate_airship_Ruby': 'Rubies!', 
	'nameplate_airship_Gems': 'The Vault Above', 
	'nameplate_airship_government': 'The Greatest Nameplate', 
	'nameplate_Airship_Hull': 'Airship Hull', 
	'nameplate_airship_Sky': 'Above The Clouds', 
	'nameplate_Polus-Skyline': 'Polus Horizon', 
	'nameplate_Polus-Snowmates': 'Snowmates of Polus', 
	'nameplate_Polus_Colors': 'Colors of Polus', 
	'nameplate_Polus_DVD': 'Simsong Stan', 
	'nameplate_Polus_Ground': 'Ground Polus', 
	'nameplate_Polus_Lava': 'Lavaly', 
	'nameplate_Polus_Planet': 'Polus Planet', 
	'nameplate_Polus_Snow': 'Snowy Lands', 
	'nameplate_Polus_SpecimenBlue': 'Specimen - Blue', 
	'nameplate_Polus_SpecimenGreen': 'Specimen - Green', 
	'nameplate_Polus_SpecimenPurple': 'Specimen - Purple', 
	'nameplate_is_yard': 'Backyard', 
	'nameplate_is_dig': 'Dig2China', 
	'nameplate_is_game': 'Sports', 
	'nameplate_is_ghost': 'Ghosts', 
	'nameplate_is_green': 'Greenery', 
	'nameplate_is_sand': 'Sandstone', 
	'nameplate_is_trees': 'Trees', 
	'nameplate_Mira_Cafeteria': "Today's Menu: Pizza Juice", 
	'nameplate_Mira_Glass': 'The Sky Below', 
	'nameplate_Mira_Tiles': 'Hive Got to do Weapons', 
	'nameplate_Mira_Vines': 'Whose Vine is it Anyway?', 
	'nameplate_Mira_Wood': 'Wood You Look at That', 
	'nameplate_hw_candy': 'Candy Time', 
	'nameplate_hw_woods': 'Spooky Woods', 
	'nameplate_hw_pumpkin': 'Jack-o-Pumpkin'
}

pets_dict = { # by Enby Cosmog. special thanks to Sharedlines for the initial version of this list
	'': 'None',
	'pet_EmptyPet': 'None', 
	'pet_Alien': 'Headslug', 
	'pet_Crewmate': 'Mini Crewmate', 
	'pet_Doggy': 'Doggy', 
	'pet_Stickmin': 'H. Stickmin', 
	'pet_Hamster': 'Hampton', 
	'pet_Robot': 'Ro-bot', 
	'pet_UFO': 'UFO', 
	'pet_Ellie': 'E. Rose', 
	'pet_Squig': 'Squig', 
	'pet_Bedcrab': 'Bedcrab', 
	'pet_test': 'Glitch', 
	'pet_Lava': 'Magmate', 
	'pet_Snow': 'Snowball', 
	'pet_Charles': 'Charles Chopper', 
	'pet_Charles_Red': 'Toppat Chopper', 
	'pet_Cube': 'Deitied Cube', 
	'pet_Bush': 'Bushfriend', 
	'pet_frankendog': 'Frankendog', 
	'pet_poro': "Heimerdinger's Poro"
}

color_indexes = (  # by SharedLines
	"Red",
	"Blue",
	"Green",
	"Pink",
	"Orange",
	"Yellow",
	"Black",
	"White",
	"Purple",
	"Brown",
	"Cyan",
	"Lime",
	"Maroon",
	"Rose",
	"Banana",
	"Gray",
	"Tan",
	"Coral",
)