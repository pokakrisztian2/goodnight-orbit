# Fact Sheet — "Every Confusing Thing About Electricity Explained Slowly (For Sleep)"

Compiled 2026-10-02 for Otto, the night-shift astronaut. Every line was checked against the listed source with WebFetch, or by downloading the page or PDF with curl/pdftotext and grepping for the exact sentence. Wikipedia was used only to find primary sources and is never cited. Old scans (Priestley 1775, Gray 1731, Du Fay 1733, Coulomb 1785, Volta 1800) were read on archive.org; long-s was changed to s and obvious OCR slips were corrected, but the wording is otherwise verbatim. French quotes are given in the original, followed by our own English gloss in [square brackets]. Some sites block bots (founders.archives.gov, parts of Britannica, the Feynman Lectures site, nobelprize.org at times), so those pages were read through a text proxy or a Wayback snapshot of the same official URL. The official URL is the one cited. A final spot-check on 2 Oct 2026 re-grepped 9 key quotes and numbers straight from the live pages: HyperPhysics drift, ENTSO-E clocks, Humboldt's horses, NOAA lightning heat, Pearl Street's 85 customers, the RI on Faraday's knighthood, Franklin's turkey, OpenStax's 4.54×10⁻⁴ m/s, and NASA's "16 sunrises and sunsets". All 9 matched.
Legend: plain line = verified. **UNCERTAIN** = not fully confirmed, disputed, or seen only in a secondary retelling. Soften it in narration or leave it out. All UNCERTAIN items are also collected at the end. **DERIVED** = our own arithmetic from a sourced number (the working is shown).

**Source key — early electricity**
"DL" = Diogenes Laertius, *Lives of Eminent Philosophers* 1.24 (Thales), tr. R. D. Hicks, Perseus/Tufts: http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0258:book=1:chapter=1
"Etym" = Online Etymology Dictionary, "electric": https://www.etymonline.com/word/electric
"Gilbert" = William Gilbert, *De Magnete* (1600), tr. P. F. Mottelay (1893), archive.org: https://archive.org/details/williamgilbertof00gilb
"Guericke1672" = Otto von Guericke, *Experimenta Nova (ut vocantur) Magdeburgica*, Amsterdam 1672 (Smithsonian Libraries copy): https://archive.org/details/ottonisdeguerick00guer
"Priestley1775" = Joseph Priestley, *The History and Present State of Electricity*, 3rd ed., London 1775: https://archive.org/details/historyandprese00priegoog
"Gray1731" = Stephen Gray, "A Letter to Cromwell Mortimer… Containing Several Experiments concerning Electricity," *Phil. Trans.* 1731: https://archive.org/details/jstor-104056
"Rice-Gray" = Galileo Project catalogue (Rice Univ., R. S. Westfall), "Gray, Stephen": http://galileo.rice.edu/Catalog/NewFiles/gray.html
"DuFay1733" = C. F. Du Fay, "A Letter… to His Grace Charles Duke of Richmond… concerning Electricity," *Phil. Trans.* 1733: https://archive.org/details/jstor-103851
"DSB-Kleist" = J. L. Heilbron, "Kleist, Ewald Georg von," *Complete Dictionary of Scientific Biography*: https://www.encyclopedia.com/science/dictionaries-thesauruses-pictures-and-press-releases/kleist-ewald-georg-von
"Leiden" = Instituut-Lorentz, Leiden University, "The Leiden jar": https://www.lorentz.leidenuniv.nl/history/fles/fles.html
"FP-1747" = Franklin to Peter Collinson, 25 May 1747, *Papers of Benjamin Franklin* vol. 3 (Yale/APS): https://franklinpapers.org/yale?vol=3&page=126b
"FP-Jul1747" = Franklin to Collinson, 28 July 1747, *Papers* vol. 3: https://franklinpapers.org/yale?vol=3&page=156a
"FP-Turkey" = Franklin to [John Franklin?], 25 Dec 1750, *Papers* vol. 4: https://franklinpapers.org/yale?vol=4&page=082a
"FP-Dalibard" = Dalibard, "Report of an Experiment with Lightning" (read to the Académie, 13 May 1752), *Papers* vol. 4: https://franklinpapers.org/yale?vol=4&page=302a
"FP-Kite" = "The Kite Experiment," Franklin's statement in the *Pennsylvania Gazette*, 19 Oct 1752, *Papers* vol. 4: https://franklinpapers.org/yale?vol=4&page=360a
"FP-Priestley" = Priestley's 1767 account of the kite, reprinted in *Papers* vol. 4: https://franklinpapers.org/yale?vol=4&page=367a
"FP-PoorRichard" = "How to secure Houses, &c. from Lightning," *Poor Richard Improved* 1753, *Papers* vol. 4: https://franklinpapers.org/yale?vol=4&page=403a
"FI" = The Franklin Institute, "Benjamin Franklin and the Kite Experiment": https://www.fi.edu/benjamin-franklin/kite-key-experiment
"APS-1752" = APS News, "May 10, 1752: First Experiment to Draw Electricity from Lightning": https://www.aps.org/publications/apsnews/200005/history.cfm
"Ars" = Jennifer Ouellette, "Your fave illustration of Franklin's kite experiment is likely riddled with errors," *Ars Technica*, May 2023 (on B. A. Moura, *Science & Education*): https://arstechnica.com/science/2023/05/your-fave-illustration-of-franklins-kite-experiment-is-likely-riddled-with-errors/
"Tucker" = Tom Tucker, *Bolt of Fate: Benjamin Franklin and His Electric Kite Hoax* (PublicAffairs, 2003), catalogue record: https://archive.org/details/boltoffatebenjam0000tuck
"Coulomb" = C. A. Coulomb, *Premier Mémoire sur l'électricité et le magnétisme* (1785), in *Collection de mémoires relatifs à la physique* vol. 1 (Société française de physique): https://archive.org/details/collectiondemm01sociuoft
"Galvani" = L. Galvani, *De viribus electricitatis…* (1791), tr. *Commentary on the Effect of Electricity on Muscular Motion* (Licht, 1953): https://archive.org/details/commentaryonthee002243mbp
"Piccolino" = M. Piccolino, *Brain Research Bulletin* 46(5):381–407 (1998), PMID 9739001: https://pubmed.ncbi.nlm.nih.gov/9739001/
"ETHW-Volta" / "ETHW-Galvani" = IEEE Engineering & Technology History Wiki: https://ethw.org/Alessandro_Volta ; https://ethw.org/Luigi_Galvani
"Volta1800" = A. Volta, "On the Electricity excited by the mere Contact of conducting Substances of different Kinds," *Phil. Trans.* 90 (1800) 403–431 (letter in French): https://archive.org/details/jstor-107060
"VoltaAbstract" = Royal Society *Proceedings* abstract of the same paper ("Read June 26, 1800"): https://archive.org/details/paper-doi-10_1098_rspl_1800_0016
"Pavia" = University of Pavia, Museo per la Storia, Volta Room: https://museoperlastoria.unipv.it/en/volta-room/
"Arago" = F. Arago, *Éloge historique d'Alexandre Volta* (1831): https://archive.org/details/eloge-historique-d-alexandre-volta
"Newgate" = *The Newgate Calendar*, "George Foster": http://www.exclassics.com/newgate/ng464.htm
"Aber" = Iwan Rhys Morus, "Frankenstein: the real experiments that inspired the fictional science," Aberystwyth University / The Conversation, Oct 2018: https://www.aber.ac.uk/en/news/archive/2018/10/title-218032-en.html
"Shelley1831" = Mary Shelley, *Frankenstein*, 1831 ed., Author's Introduction, Project Gutenberg #42324: https://www.gutenberg.org/ebooks/42324

**Source key — what electricity is, and the field pioneers**
"NOBEL-JJT" / "NOBEL-JJT-BIO" = Nobel Prize Outreach, J.J. Thomson – Facts / Biographical: https://www.nobelprize.org/prizes/physics/1906/thomson/facts/ ; https://www.nobelprize.org/prizes/physics/1906/thomson/biographical/
"RI-JJT" = Royal Institution, "Subatomic science: JJ Thomson's discovery of the electron": https://www.rigb.org/explore-science/explore/blog/subatomic-science-jj-thomsons-discovery-electron
"APS-ELEC" = APS News, This Month in Physics History, "Discovery of the electron" (Oct 2000): https://www.aps.org/apsnews/2000/10/discovery-of-the-electron
"BRIT-JJT" = Encyclopaedia Britannica, "J.J. Thomson": https://www.britannica.com/biography/J-J-Thomson
"NOBEL-MIL" = Nobel Prize Outreach, Robert A. Millikan – Facts: https://www.nobelprize.org/prizes/physics/1923/millikan/facts/
"MIL-LECT" = R. A. Millikan, Nobel Lecture, 23 May 1924: https://www.nobelprize.org/uploads/2018/06/millikan-lecture.pdf
"APS-MIL" = APS News, "Robert Millikan oil drop results" (Aug 2006): https://www.aps.org/apsnews/2006/08/robert-millikan-oil-drop-results
"NIST-AMP" = NIST, "Ampere: Introduction" (SI redefinition): https://www.nist.gov/si-redefinition/ampere-introduction
"NIST-E" = NIST CODATA, elementary charge: https://physics.nist.gov/cgi-bin/cuu/Value?e
"BIPM-AMP" = BIPM, SI base unit: ampere: https://www.bipm.org/en/si-base-units/ampere
"BIPM-SI" = BIPM, *The International System of Units* (SI Brochure, 9th ed.): https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf
"HP-CUR" / "HP-VOLT" / "HP-WATER" / "HP-DRIFT" / "HP-OHM" = R. Nave, HyperPhysics (Georgia State Univ.): "Electric Current" http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elecur.html ; "Voltage" http://hyperphysics.phy-astr.gsu.edu/hbase/electric/elevol.html ; "Water Analogy to DC Circuits" http://hyperphysics.phy-astr.gsu.edu/hbase/electric/watcir.html ; "Microscopic View of Electric Current" http://hyperphysics.phy-astr.gsu.edu/hbase/electric/miccur.html ; "Microscopic View of Ohm's Law" http://hyperphysics.phy-astr.gsu.edu/hbase/electric/ohmmic.html
"OSX-9.2" = OpenStax, *University Physics* Vol. 2, §9.2 "Model of Conduction in Metals": https://openstax.org/books/university-physics-volume-2/pages/9-2-model-of-conduction-in-metals
"FEYN-II-1" / "FEYN-II-24" / "FEYN-II-27" = R. P. Feynman, *Feynman Lectures on Physics* Vol. II, chs. 1, 24, 27 (Caltech): https://www.feynmanlectures.caltech.edu/II_01.html ; https://www.feynmanlectures.caltech.edu/II_24.html ; https://www.feynmanlectures.caltech.edu/II_27.html
"BRIT-OHM" = Encyclopaedia Britannica, "Georg Ohm": https://www.britannica.com/biography/Georg-Ohm
"MACTUTOR-OHM" = O'Connor & Robertson, MacTutor (Univ. St Andrews), "Georg Simon Ohm": https://mathshistory.st-andrews.ac.uk/Biographies/Ohm/
"ETHW-OHM" = IEEE ETHW, "Georg Simon Ohm": https://ethw.org/Georg_Simon_Ohm
"APS-OER" = APS News, "July 1820: Oersted & Electromagnetism" (2008): https://www.aps.org/apsnews/2008/07/1820-oersted-electromagnetism
"ETHW-OER" = IEEE ETHW, "Hans Christian Oersted": https://ethw.org/Hans_Christian_Oersted
"BRIT-ORS" / "BRIT-AMP" = Encyclopaedia Britannica, "Hans Christian Ørsted" / "André-Marie Ampère": https://www.britannica.com/biography/Hans-Christian-Orsted ; https://www.britannica.com/biography/Andre-Marie-Ampere
"RI-FARADAY" = Royal Institution, Michael Faraday (1791–1867): https://www.rigb.org/explore-science/explore/person/michael-faraday-1791-1867
"RI-NOTEBOOKS" = Royal Institution, "Notebooks preview: note-taking life of young Michael Faraday": https://www.rigb.org/explore-science/explore/blog/notebooks-preview-note-taking-life-young-michael-faraday
"RI-MOTOR" = Royal Institution (Charlotte New), "The birth of electric motion": https://www.rigb.org/explore-science/explore/blog/birth-electric-motion
"RI-MOTOR-OBJ" / "RI-RING" / "RI-GEN" / "RI-IRON" = Royal Institution collection pages: motor https://www.rigb.org/explore-science/explore/collection/michael-faradays-electric-magnetic-rotation-apparatus-motor ; ring https://www.rigb.org/explore-science/explore/collection/michael-faradays-ring-coil-apparatus ; generator https://www.rigb.org/explore-science/explore/collection/michael-faradays-generator ; iron filings https://www.rigb.org/explore-science/explore/collection/michael-faradays-iron-filings
"RI-XMAS" = Royal Institution, History of the CHRISTMAS LECTURES: https://www.rigb.org/christmas-lectures/history-christmas-lecturesr
"BRIT-FAR" = Encyclopaedia Britannica, "Michael Faraday": https://www.britannica.com/biography/Michael-Faraday
"APS-FAR" = APS News, "Faraday & electromagnetism" (Aug 2001): https://www.aps.org/apsnews/2001/08/faraday-electromagnetism
"LECKY-1899" = W. E. H. Lecky, *Democracy and Liberty*, new ed., Introduction p. xxxi (Longmans, 1899): https://archive.org/details/cu31924024864617
"MAXWELL-1862" = J. C. Maxwell, "On Physical Lines of Force," Part III, *Phil. Mag.* (1862), transcription on Wikisource: https://en.wikisource.org/wiki/On_Physical_Lines_of_Force
"MAXWELL-1865" = J. C. Maxwell, "A Dynamical Theory of the Electromagnetic Field," *Phil. Trans.* 155 (1865), transcription on Wikisource: https://en.wikisource.org/wiki/A_Dynamical_Theory_of_the_Electromagnetic_Field
"BRIT-MAX" / "ETHW-MAX" = Britannica, "James Clerk Maxwell": https://www.britannica.com/biography/James-Clerk-Maxwell ; IEEE ETHW, "James Clerk Maxwell": https://ethw.org/James_Clerk_Maxwell
"BRIT-HERTZ" / "ETHW-HERTZ" / "BRIT-EM" = Britannica, "Heinrich Hertz": https://www.britannica.com/biography/Heinrich-Hertz ; ETHW, "Heinrich Hertz": https://ethw.org/Heinrich_Hertz ; Britannica, "Electromagnetism – Faraday's discovery of electric induction": https://www.britannica.com/science/electromagnetism/Faradays-discovery-of-electric-induction

**Source key — power to the people**
"NPS-Light" = National Park Service, Thomas Edison NHP, "The Electric Light System": https://www.nps.gov/edis/learn/kidsyouth/the-electric-light-system-phonograph-motion-pictures.htm
"Brit-Edison" / "Brit-Tesla" / "Brit-Westinghouse" / "Brit-Electrocution" / "Brit-Columbian" = Encyclopaedia Britannica: https://www.britannica.com/biography/Thomas-Edison ; https://www.britannica.com/biography/Nikola-Tesla ; https://www.britannica.com/biography/George-Westinghouse ; https://www.britannica.com/topic/electrocution ; https://www.britannica.com/event/Worlds-Columbian-Exposition
"EdisonPapers-Light" / "EdisonPapers-Bio" = Thomas A. Edison Papers, Rutgers: "Electric Light and Power System" https://edison.rutgers.edu/life-of-edison/inventions?view=article&id=532:electric-light-and-power-system&catid=91:inventions ; "Biography" https://edison.rutgers.edu/life-of-edison/biography
"ETHW-Pearl" = IEEE/ETHW, "Milestones: Pearl Street Station, 1882": https://ethw.org/Milestones:Pearl_Street_Station,_1882
"ETHW-EarlyApps" / "ETHW-Hammer" = ETHW, "Early Applications of Electric Power" https://ethw.org/Early_Applications_of_Electric_Power ; "William Joseph Hammer" https://ethw.org/William_Joseph_Hammer
"ETHW-Stanley" = IEEE/ETHW, "Milestones: Alternating Current Electrification, 1886": https://ethw.org/Milestones:Alternating_Current_Electrification,_1886
"ETHW-Adams" = IEEE/ETHW, "Milestones: Adams Hydroelectric Generating Plant, 1895": https://ethw.org/Milestones:Adams_Hydroelectric_Generating_Plant,_1895
"ETHW-Buffalo" = Craig A. Woodworth, "Early Electrification of Buffalo," IEEE/ETHW: https://ethw.org/Early_Electrification_of_Buffalo
"ETHW-Tesla" / "ETHW-WEC" = ETHW, "Nikola Tesla" https://ethw.org/Nikola_Tesla ; "Westinghouse Electric Corporation" https://ethw.org/Westinghouse_Electric_Corporation
"Martin1894" = T. C. Martin, *The Inventions, Researches and Writings of Nikola Tesla* (1894), Project Gutenberg #39272: https://www.gutenberg.org/ebooks/39272
"Tesla-MyInventions" = Nikola Tesla, "My Inventions," Part IV, *Electrical Experimenter* (1919), Tesla Universe transcription: https://teslauniverse.com/nikola-tesla/articles/my-inventions-iv-discovery-tesla-coil-and-transformer
"Patent381968" = N. Tesla, US Patent 381,968, "Electro-magnetic motor": https://patents.google.com/patent/US381968A/en
"Smithsonian-Topsy" = Kat Eschner, "Topsy the Elephant Was a Victim of Her Captors, Not Thomas Edison," *Smithsonian*, 4 Jan 2017: https://www.smithsonianmag.com/smart-news/topsy-elephant-was-victim-her-captors-not-really-thomas-edison-180961611/
"TaskForce2003" = U.S.-Canada Power System Outage Task Force, *Final Report on the August 14, 2003 Blackout* (April 2004): https://www.energy.gov/sites/default/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
"Udry1970" = J. R. Udry, "The effect of the Great Blackout of 1965 on births in New York City," *Demography* 7(3):325–327 (1970): https://doi.org/10.2307/2060151
"NREL-Inertia" = P. Denholm et al., *Inertia and the Power Grid: A Guide Without the Spin*, NREL/TP-6A20-73856 (May 2020): https://docs.nlr.gov/docs/fy20osti/73856.pdf
"EIA-Delivery" / "EIA-2016" / "EIA-Plants" / "EIA-Losses" = U.S. Energy Information Administration: https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php ; https://www.eia.gov/todayinenergy/detail.php?id=27152 ; https://www.eia.gov/tools/faqs/faq.php?id=65 ; https://www.eia.gov/tools/faqs/faq.php?id=105
"IEA-2025" / "IEA-2026" = IEA, *Electricity 2025* and *Electricity 2026*, executive summaries: https://www.iea.org/reports/electricity-2025/executive-summary ; https://www.iea.org/reports/electricity-2026/executive-summary
"NESO-Euro2020" = National Grid ESO (now NESO), "EURO 2020 and the TV 'pick-up' effect," 1 Jul 2021: https://www.neso.energy/news/euro-2020-and-tv-pick-effect
"ESO-Lockdown" = National Grid ESO, "The 'lockdown effect' on TV viewing habits and the electricity grid," 6 Apr 2020: https://www.nationalgrideso.com/news/lockdown-effect-tv-viewing-habits-and-electricity-grid
"ENTSOE-2018" = ENTSO-E press release, "Continuing frequency deviation in the Continental European Power System originating in Serbia/Kosovo…," 6 Mar 2018: https://www.entsoe.eu/news/2018/03/06/press-release-continuing-frequency-deviation-in-the-continental-european-power-system-originating-in-serbia-kosovo-political-solution-urgently-needed-in-addition-to-technical/
"ENTSOE-IbPage" = ENTSO-E, "28 April 2025 Blackout" investigation page: https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/
"ENTSOE-IbFinal" = ENTSO-E Expert Panel, Final Report on the Grid Incident in Spain and Portugal on 28 April 2025 (20 Mar 2026): https://eepublicdownloads.blob.core.windows.net/public-cdn-container/clean-documents/Publications/2025/iberian-blackout/Final%20Report%20on%20the%20Grid%20Incident%20in%20Spain%20and%20Portugal%20on%2028%20April%202025.pdf
"ENTSOE-IbFactual" = ENTSO-E Expert Panel, Factual Report (3 Oct 2025): https://eepublicdownloads.blob.core.windows.net/public-cdn-container/clean-documents/Publications/2025/iberian-blackout/entso-e_incident_report_ES-PT_April_2025_06.pdf
"ENTSOE-IbBrief" = ENTSO-E, Expert Panel Final Report – Media Briefing slides (20 Mar 2026): https://eepublicdownloads.blob.core.windows.net/public-cdn-container/clean-documents/Publications/2025/iberian-blackout/260318_Final%20report_press%20briefing%20PPT_Final.pdf
"ENTSOE-0428" / "ENTSOE-0619" = ENTSO-E news, 28 Apr 2025 and 19 Jun 2025: https://www.entsoe.eu/news/2025/04/28/grid-incident-in-the-power-systems-of-spain-and-portugal/ ; https://www.entsoe.eu/news/2025/06/19/expert-panel-will-review-the-reports-on-the-28th-april-blackout-published-this-week-by-the-spanish-government-and-the-spanish-tso/

**Source key — nature, bodies, batteries, space**
"NWS-Overview" / "NWS-Temp" / "NWS-Power" / "NWS-Myths" / "NWS-Cars" = NOAA National Weather Service lightning pages: https://www.weather.gov/safety/lightning-science-overview ; https://www.weather.gov/safety/lightning-temperature ; https://www.weather.gov/safety/lightning-power ; https://www.weather.gov/safety/lightning-myths ; https://www.weather.gov/safety/lightning-cars
"NSSL-FAQ" / "NSSL-Types" = NOAA National Severe Storms Laboratory, Severe Weather 101: Lightning FAQ / Types: https://www.nssl.noaa.gov/education/svrwx101/lightning/faq/ ; https://www.nssl.noaa.gov/education/svrwx101/lightning/types/
"Christian2003" = H. J. Christian et al., "Global frequency and distribution of lightning as observed from space by the Optical Transient Detector," *J. Geophys. Res.* (2003): https://doi.org/10.1029/2002JD002347
"Albrecht2016" = R. I. Albrecht et al., "Where Are the Lightning Hotspots on Earth?", *Bull. Amer. Meteor. Soc.* 97(11) (2016): https://journals.ametsoc.org/view/journals/bams/97/11/bams-d-14-00193.1.xml
"NASA-SVS-Schumann" = NASA Goddard SVS, "Schumann Resonance" (#10891): https://svs.gsfc.nasa.gov/10891/
"NASA-Sprites" = NASA Heliophysics, "Seeing Sprites" (Wayback snapshot, Aug 2022): http://web.archive.org/web/20220825131452/https://www.nasa.gov/mission_pages/sunearth/news/seeing-sprites.html
"APOD-Sprite" = NASA APOD, "Sprite Lightning at 100,000 Frames Per Second," 4 Jan 2021: https://apod.nasa.gov/apod/ap210104.html
"Franz1990" = R. C. Franz, R. J. Nemzek & J. R. Winckler, "Television image of a large upward electrical discharge above a thunderstorm system," *Science* 249:48–51 (1990): https://pubmed.ncbi.nlm.nih.gov/17787625/
"ESA-ASIM" = ESA, "Atmosphere–Space Interactions Monitor": https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Research/Atmosphere_Space_Interactions_Monitor
"OS-AP-12.4" / "OS-AP-19.2" / "OS-Phys-20.7" = OpenStax *Anatomy & Physiology 2e* 12.4 and 19.2; *College Physics 2e* 20.7: https://openstax.org/books/anatomy-and-physiology-2e/pages/12-4-the-action-potential ; https://openstax.org/books/anatomy-and-physiology-2e/pages/19-2-cardiac-muscle-and-electrical-activity ; https://openstax.org/books/college-physics-2e/pages/20-7-nerve-conduction-electrocardiograms
"Sonawane2023" = K. Sonawane et al., *Cureus* (2023): https://doi.org/10.7759/cureus.41771
"Tsubo2024" = T. Tsubo, "Neuron with well-designed ionic system," *Biophysics and Physicobiology* (2024): https://doi.org/10.2142/biophysico.bppb-v21.0028
"Nobel1963" / "Nobel1963-Speed" / "Nobel1963-Speech" = NobelPrize.org, Physiology or Medicine 1963 summary, speed read and ceremony speech: https://www.nobelprize.org/prizes/medicine/1963/summary/ ; https://www.nobelprize.org/prizes/medicine/1963/speedread/ ; https://www.nobelprize.org/prizes/medicine/1963/ceremony-speech/
"Nobel1924" / "Nobel1924-Speech" = NobelPrize.org, Physiology or Medicine 1924 summary and ceremony speech: https://www.nobelprize.org/prizes/medicine/1924/summary/ ; https://www.nobelprize.org/prizes/medicine/1924/ceremony-speech/
"Ornes2025" = S. Ornes, "Can neuromorphic computing help reduce AI's high energy cost?", *PNAS* news feature (2025): https://doi.org/10.1073/pnas.2528654122
"Humboldt-PN2" = A. von Humboldt & A. Bonpland, *Personal Narrative of Travels to the Equinoctial Regions of America*, Vol. 2, tr. T. Ross, Project Gutenberg #7014: https://www.gutenberg.org/ebooks/7014
"Catania2016" = K. C. Catania, "Leaping eels electrify threats, supporting Humboldt's account of a battle with horses," *PNAS* 113(25):6979–84 (2016): https://doi.org/10.1073/pnas.1604009113
"Catania2017" = K. C. Catania, "Power Transfer to a Human during an Electric Eel's Shocking Leap," *Current Biology* 27(18) (2017): https://pubmed.ncbi.nlm.nih.gov/28918950/
"Catania2019" = K. C. Catania, "The Astonishing Behavior of Electric Eels," *Frontiers in Integrative Neuroscience* 13:23 (2019): https://pmc.ncbi.nlm.nih.gov/articles/PMC6646469/
"deSantana2019" = C. D. de Santana et al., "Unexpected species diversity in electric eels with a description of the strongest living bioelectricity generator," *Nature Communications* 10:4000 (2019): https://www.nature.com/articles/s41467-019-11690-z
"Bray2022" = I. E. Bray et al., "The diversity and evolution of electric organs in Neotropical knifefishes," *EvoDevo* (2022): https://doi.org/10.1186/s13227-022-00194-5
"Bellono2017" = N. W. Bellono, D. B. Leitch & D. Julius, *Nature* 543:391–396 (2017): https://pubmed.ncbi.nlm.nih.gov/28264196/
"Scheich1986" = H. Scheich et al., "Electroreception and electrolocation in platypus," *Nature* 319:401–402 (1986): https://pubmed.ncbi.nlm.nih.gov/3945317/
"Nobel2019-PR" / "Nobel2019-Pop" = Royal Swedish Academy of Sciences, Chemistry 2019 press release and popular information: https://www.nobelprize.org/prizes/chemistry/2019/press-release/ ; https://www.nobelprize.org/prizes/chemistry/2019/popular-information/
"Nobel-Goodenough" / "Nobel-Facts" = NobelPrize.org, John B. Goodenough – Facts; Nobel Prize facts: https://www.nobelprize.org/prizes/chemistry/2019/goodenough/facts/ ; https://www.nobelprize.org/prizes/facts/nobel-prize-facts/
"Nobel1956" = NobelPrize.org, Physics 1956 summary: https://www.nobelprize.org/prizes/physics/1956/summary/
"CHM-1947" / "CHM-1940" = Computer History Museum, *The Silicon Engine*: https://www.computerhistory.org/siliconengine/invention-of-the-point-contact-transistor/ ; https://www.computerhistory.org/siliconengine/discovery-of-the-p-n-junction/
"Apple-A14" = Apple Newsroom, iPad Air with A14 Bionic, Sept 2020: https://www.apple.com/newsroom/2020/09/apple-unveils-all-new-ipad-air-with-a14-bionic-apples-most-advanced-chip/
"NASA-ISS-Facts" = NASA, "International Space Station Facts and Figures": https://www.nasa.gov/international-space-station/space-station-facts-and-figures/
"NASA-Glenn-EPS" = NASA Glenn, "NASA Glenn Contributions to the ISS Electrical Power System" fact sheet (Wayback, Jun 2023): https://web.archive.org/web/20230606091157/https://www.nasa.gov/centers/glenn/about/fs06grc.html
"NASA-Blog-Batt" / "NASA-Blog-iROSA21" / "NASA-Blog-iROSA23" = NASA Space Station Blog, 1 Feb 2021; 16 Jun 2021; 9 Jun 2023: https://blogs.nasa.gov/spacestation/2021/02/01/spacewalkers-wrap-up-battery-work-and-camera-installations/ ; https://blogs.nasa.gov/spacestation/2021/06/16/spacewalk-to-install-first-new-solar-array-concluded/ ; https://blogs.nasa.gov/spacestation/2023/06/09/nasa-spacewalkers-complete-solar-array-installation/
"NASA-NESC-Charging" = NASA Engineering and Safety Center, "Understanding the Potential Dangers of Spacecraft Charging," 12 Jan 2017: https://www.nasa.gov/centers-and-facilities/nesc/understanding-the-potential-dangers-of-spacecraft-charging/
"NOAA-SWPC-Aurora" = NOAA Space Weather Prediction Center, "Aurora": https://www.swpc.noaa.gov/phenomena/aurora
"NASA-EO-Black" = NASA Earth Observatory, "Out of the Blue and Into the Black," 5 Dec 2012: https://science.nasa.gov/earth/earth-observatory/out-of-the-blue-and-into-the-black/
"NASA-BlackMarble" = NASA, "Black Marble" (2012): https://www.nasa.gov/image-article/black-marble/
"Faraday-Candle" = Michael Faraday (ed. W. Crookes), *The Chemical History of a Candle*, Project Gutenberg #14474: https://www.gutenberg.org/ebooks/14474

> Corrections to the brief:
> - **"Electrons rush down the wire at the speed of light": no.** In ordinary household copper wire, electrons drift at roughly a few tenths of a millimetre per second. OpenStax's worked example gives 4.54×10⁻⁴ m/s at 20 A (OSX-9.2). What moves at "a significant fraction of the speed of light" is the *change in the electric field* (OSX-9.2). On AC mains the electrons hardly travel at all; they rock back and forth in place. The full answer is the through-line in section 23.
> - **"Energy flows inside the wire like water in a pipe": no.** Feynman: the electrons get their energy "because of the energy flowing into the wire from the field outside" (FEYN-II-27). The water analogy is useful, but HyperPhysics itself says "All such analogies have their drawbacks" (HP-WATER).
> - **"Current flows the wrong way."** Partly right. Franklin's 1747 plus/minus labels came 150 years before anyone knew what moves (FP-1747). When Thomson's particles turned out to carry the "negative" charge (APS-ELEC), the convention stayed: "it has long been the convention to take the direction of electric current as if it were the positive charges which are moving" (HP-CUR). Conventional current is Franklin's arrow; in a wire, the electrons drift against it. Nothing is broken. It is only a naming accident.
> - **Franklin's kite: it was not struck by lightning, and Franklin was not first.** "To dispel another myth, Franklin's kite was not struck by lightning" (FI). The kite collected charge from the storm's field. The first electricity drawn from a thunderstorm was at Marly-la-Ville, France, on 10 May 1752, using Franklin's proposed design, about a month *before* the kite (FP-Dalibard; FP-Priestley). Franklin also stood "within a Door, or Window, or under some Cover" (FP-Kite). And William Franklin was 21, not the little boy of the paintings (Ars).
> - **"Did the kite even happen?"** Franklin's Gazette text reads like instructions and "never confirmed in the text whether the experiment was performed" (Ars). Tom Tucker's *Bolt of Fate* (2003) argues it was a hoax (Tucker). That is a minority view. The detailed account is Priestley's (1767), written with Franklin's input, and most historians accept it. Say: "most historians believe he did fly it; one writer has argued he didn't."
> - **The Leyden jar wasn't first made in Leiden.** Ewald von Kleist, a cathedral dean in Pomerania, described the effect on 4 November 1745 (Priestley1775; DSB-Kleist). Leiden came early in 1746.
> - **Musschenbroek's "not for the kingdom of France"** is Priestley's English paraphrase of a French letter, so it is reported speech and not his exact words (Priestley1775). Leiden University paraphrases it as "the whole kingdom of France could not compel him to repeat the experience" (Leiden).
> - **Faraday's "What use is a newborn baby?" and "Sir, you may soon be able to tax it."** Neither has a Faraday source. The baby line is attached to Franklin watching a balloon in 1783, and even that version is examined as "A Legendary Bon Mot?" (S. L. Chapin, *Proc. Amer. Philos. Soc.* 129:3, 1985). The tax story's earliest print appearance we found is hearsay from 1899, 32 years after Faraday died, from an unnamed friend. It does not mention electricity, and the questioner is Gladstone (LECKY-1899). Say: "a story told about Faraday, first printed long after his death."
> - **"Faraday refused a knighthood":** "He publicly stated several times that he would not accept a knighthood, but no evidence has been found that he was ever offered one" (RI-FARADAY).
> - **"Faraday gave the first Christmas Lectures":** he *founded* them in 1825. John Millington gave the first series; Faraday gave the second, and 19 in all (RI-XMAS).
> - **"Thomson named the electron":** Stoney coined "electron" in 1891. Thomson said "corpuscles" (APS-ELEC; RI-JJT).
> - **The famous Maxwell light line** ("we can scarcely avoid the inference…") is from *On Physical Lines of Force*, Part III (1862), not the 1865 *Dynamical Theory* (MAXWELL-1862).
> - **"Edison invented the light bulb":** "Thomas Alva Edison did not invent the first light bulb." He made "the first incandescent light that was practical" and a whole system around it (NPS-Light; Brit-Edison).
> - **Pearl Street's "500 customers" were a year later.** On day one there were "only some 85 customers having a total of about 400 lamps" (ETHW-Pearl).
> - **Topsy the elephant (1903) was not part of the War of the Currents,** which "ended in the 1890s". Smithsonian, citing the Edison Papers, says "it's unlikely that Edison was a direct part of Topsy's execution or even saw it" (Smithsonian-Topsy). Leave Topsy out of a sleep video either way.
> - **Tesla's "$50,000" story** comes only from Tesla's own 1919 memoir, and even there he blames "The Manager", not Edison: "The Manager had promised me fifty thousand dollars… but it turned out to be a practical joke" (Tesla-MyInventions). There is no independent record.
> - **Edison's "I have not failed, I've found 10,000 ways…"** is not used anywhere in this sheet. It has no reliable source.
> - **The "1965 blackout baby boom" is false.** Births nine months later showed "no increase… associated with the blackout" (Udry1970).
> - **Niagara's two dates:** first power to local industry on 26 Aug 1895 (ETHW-Adams); power reached Buffalo, 22 miles away, on 15 Nov 1896 (ETHW-Buffalo).
> - **"Lightning is hotter than the Sun's surface":** true for the *air* it heats, about 50,000 °F, "5 times hotter than the surface of the sun" (NWS-Temp). Strictly, "lightning is the movement of electrical charges and doesn't have a temperature" (NWS-Temp).
> - **"Lightning never strikes twice," "rubber tyres protect you," "lightning victims stay electrified":** all false (NWS-Myths; NWS-Cars).
> - **Electric eels are not eels.** They are South American knifefishes (Gymnotiformes) (Bray2022). There are three species, not one (deSantana2019).
> - **ISS power "240 kW"** could not be confirmed on any NASA page. NASA's own facts page says "8 solar arrays provide 75 to 90 kilowatts of power" (NASA-ISS-Facts). The older Glenn sheet says 110 kW for the US and Russian systems combined (NASA-Glenn-EPS). Each new iROSA gives "more than 20 kilowatts" (NASA-Blog-iROSA23). Use "about a hundred kilowatts, roughly what fifty-odd houses use."

---

## 0. Intro toolkit — the words we will use

- **Elementary charge (e):** the smallest free packet of charge. Since 20 May 2019 it is fixed by definition at exactly 1.602 176 634 × 10⁻¹⁹ coulomb, standard uncertainty "(exact)". — NIST-E; NIST-AMP
- **Coulomb:** "One coulomb is equal to about 6.241 x 10 18 electric charges ( e )." That is about six and a quarter billion billion electrons. — NIST-AMP
- **Ampere (current):** "One ampere is the current in which one coulomb of charge travels across a given point in 1 second." — NIST-AMP
- BIPM's formal wording: "one ampere is the electric current corresponding to the flow of 1/(1.602 176 634 x 10 –19 ) elementary charges per second." — BIPM-AMP
- **Voltage:** "Voltage is electric potential energy per unit charge, measured in joules per coulomb ( = volts)." — HP-VOLT
- "Electric potential difference is also called 'voltage' in many countries, as well as 'electric tension' or simply 'tension' in some countries." — BIPM-SI
- **The volt (1946 wording):** "The volt is the potential difference between two points of a conducting wire carrying a constant current of 1 ampere, when the power dissipated between these points is equal to 1 watt." — BIPM-SI (Appendix 1)
- **The ohm (1946 wording):** "The ohm is the electric resistance between two points of a conductor when a constant potential difference of 1 volt, applied to these points, produces in the conductor a current of 1 ampere". — BIPM-SI
- **The coulomb (1946 wording):** "The coulomb is the quantity of electricity carried in 1 second by a current of 1 ampere." — BIPM-SI
- In today's SI table: coulomb = A·s; volt = W/A; ohm = V/A. — BIPM-SI
- "Electromotive force" is a misnomer: it is "not a 'force'. The term emf is retained for historical reasons." — HP-VOLT
- A feel for a coulomb: "One Coulomb of charge is the charge which would flow through a 120 watt lightbulb (120 volts AC) in one second." — HP-CUR
- And how strong it is: two one-coulomb charges a metre apart "would repel each other with a force of about a million tons!" — HP-CUR
- Everyday currents: a hair dryer draws "15 amps for an 1,800-watt model"; "a lightning bolt can carry 100,000 amps or more". — NIST-AMP
- Yet "an average lightning bolt carries around 5 coulombs of charge, even though its current may be tens of thousands of amps", because it lasts only tens of milliseconds. — NIST-AMP
- e is "about a tenth of a billionth of a billionth of the amount of charge in a current of 1 ampere that moves past a given point in 1 second." — NIST-AMP
- **Conventional current:** "it has long been the convention to take the direction of electric current as if it were the positive charges which are moving." — HP-CUR

## 1. Rubbed Amber (Thales, Gilbert, Guericke, Gray, Du Fay)

- Diogenes Laertius on Thales: "Aristotle and Hippias affirm that, arguing from the magnet and from amber, he attributed a soul or life even to inanimate objects." — DL
- Aristotle's own surviving remark mentions only the lodestone: Thales "said that this stone has a soul, since it moves iron." So the amber detail comes through later reporting. — Gilbert (Mottelay's footnote quoting *De Anima*); DL
- Greek *ēlektron* meant "amber" (in Homer, Hesiod and Herodotus) and also "pale gold", an alloy of "1 part silver to 4 of gold". — Etym
- "Electric" was "apparently coined as Modern Latin electricus (literally "resembling amber") by English physicist William Gilbert (1540-1603) in treatise "De Magnete" (1600)". — Etym
- Gilbert's Latin: "Vim illam electricam nobis placet appellare". In translation: "for it pleases us to call electric force that force which has its origin in humors". — Etym; Gilbert
- The word reached English in the "1640s, first used in English by physician Sir Thomas Browne". — Etym
- Gilbert's translator: he "was the first to use the terms "electric force," "electric emanations," and "electric attraction."" — Gilbert (Mottelay intro)
- **The first electroscope (the versorium):** "make yourself a rotating-needle (electroscope — versorium) of any sort of metal, three or four fingers long, pretty light, and poised on a sharp point after the manner of a magnetic pointer." — Gilbert
- "Bring near to one end of it a piece of amber or a gem, lightly rubbed, polished and shining: at once the instrument revolves." — Gilbert
- Amber wasn't alone. Diamond, sapphire, opal, amethyst, rock crystal, glass, sulphur and sealing-wax also attract when rubbed. Gilbert called them "electrics": "Bodies that attract in the same way as amber." — Gilbert
- He scolded older writers for stories "disgracefully inaccurate", such as the claim that amber would not attract basil leaves. — Gilbert
- Otto von Guericke's electrical experiments appear in *Experimenta Nova (ut vocantur) Magdeburgica*, Amsterdam, 1672. — Guericke1672
- He cast a ball of sulphur inside a glass globe and then broke the glass. Priestley: "He little imagined that the glass globe itself, with or without the sulphur, would have answered his purpose as well." — Priestley1775
- "This globe of sulphur he mounted upon an axis, and whirled it in a wooden frame, rubbing it at the same time with his hand". — Priestley1775
- He saw repulsion: "he kept a feather a long time suspended in the air above his sulphur globe". — Priestley1775
- "he was obliged to hold his ear near the globe to perceive the hissing sound of the electric fire". — Priestley1775
- Stephen Gray was baptised in Canterbury on 26 Dec 1666 and worked as a dyer like his father. He became a pensioner of the Charterhouse "through the patronage of Prince of Wales, 1719 until his death." — Rice-Gray
- Gray was the "First receipient of the Copley medal, 1731, and then again in 1732." — Rice-Gray
- On 2 July 1729, in Granville Wheler's gallery, they carried the "electric virtue" along a line "eighty feet and a half in length", held up by silk. — Priestley1775
- When the silk broke they tried thin brass wire, and the charge vanished: "It had all gone off by the brass wire which supported it." The supports had to be silk, an insulator. — Priestley1775
- In the end they "conveyed the electric virtue seven hundred and sixty-five feet". — Priestley1775
- Wheler "electrified a red-hot poker" and "suspended a live chicken upon the tube by the legs". — Priestley1775
- Gray's own words: "April 8, 1730, I made the following Experiment on a Boy between eight and nine Years of Age. His Weight, with his Cloaths on, was forty-seven Pounds ten Ounces." — Gray1731
- "I suspended him in a horizontal Position, by two Hair-Lines, such as Cloaths are dried on: They were about thirteen Feet long". — Gray1731
- Leaf-brass jumped up toward the boy's face "to the Hight of eight, and sometimes ten Inches"; on a later trial "more than twelve Inches". — Gray1731
- The popular "charity boy on silk cords" detail is **UNCERTAIN (Gray's paper says only "a Boy", hung on hair lines, not silk)**. — Gray1731
- Du Fay, 1733: "Chance has thrown in my way another Principle, more universal and remarkable than the preceding one, and which casts a new Light on the Subject of Electricity." — DuFay1733
- "This Principle is, that there are two distinct Electricities, very different from one another; one of which I call vitreous Electricity, and the other resinous Electricity." — DuFay1733
- "The first is that of Glass, Rock-Crystal, Precious Stones, Hair of Animals, Wool, and many other Bodies: The second is that of Amber, Copal, Gum-Lack, Silk, Thread, Paper, and a vast Number of other Substances." — DuFay1733
- His rule: a vitreous body "repels all such as are of the same Electricity; and on the contrary, attracts all those of the resinous Electricity". — DuFay1733

## 2. The Jar That Bit (Leyden jar, Nollet, Franklin's plus and minus)

- Priestley: "THE end of the year 1745, and the beginning of 1746 were famous for the most surprising discovery that has yet been made in the whole business of electricity". — Priestley1775
- "the person who first made this great discovery, was Mr. Von Kleist, dean of the cathedral in Camin; who, on the 4th of November 1745, sent an account of it to Dr. Lieberkuhn at Berlin." — Priestley1775
- Kleist put a nail in a "narrow-necked medicine glass". He wrote in December 1745: "What really surprises me… is that the powerful effect occurs only [when the bottle is held] in the hand". — DSB-Kleist
- No one could repeat Kleist's result until Musschenbroek described "a similar chance experiment done at Leiden toward the beginning of 1746". — DSB-Kleist
- Priestley says the "Leyden phial" got its name "because made by Mr. Cuneus a native of Leyden". — Priestley1775
- Musschenbroek's shock, as reported by Priestley: "he felt himself struck in his arms, shoulder and breast, so that he lost his breath, and was two days before he recovered from the effects of the blow and the terror. He adds, that he would not take a second shock for the kingdom of France". — Priestley1775 **UNCERTAIN (Priestley's English paraphrase of a French letter to Réaumur; exact words and date unverified)**
- Leiden University's version: "the whole kingdom of France could not compel him to repeat the experience." — Leiden
- Allamand found that only Bohemian glass worked: "he had tried English glasses without any effect at all". — Priestley1775
- "From this time it became the subject of general conversation." — Priestley1775
- "numbers of persons, in almost every country in Europe, got a livelihood by going about and showing it." — Priestley1775
- Abbé Nollet "entertained the court at Versailles by causing a company of 180 royal guardsmen to jump simultaneously" (1746). — Aber
- A French human chain "was made of nine hundred toises, consisting of men holding iron wires betwixt each two, through which the electric shock was sensibly felt." — Priestley1775
- Another shock ran through a wire "two thousand toises in length, that is near a Paris league, or about two English miles and a half". — Priestley1775
- Leiden says the shows "culminated in one involving 700 monks joined in a circle". The popular "200 Carthusian monks" figure is **UNCERTAIN (no fetched source)**. — Leiden
- **Plus and minus are born.** Franklin to Collinson, 25 May 1747: "Hence have arisen some new Terms among us. We say B (and other Bodies alike circumstanced) are electrised positively; A negatively: Or rather B is electrised plus and A minus." — FP-1747
- "And we daily in our Experiments electrise Bodies plus or minus as we think proper." — FP-1747
- His one-fluid idea: rubbed glass parts "do, in the Instant of the Friction, attract the Electrical Fire, and therefore take it from the Thing rubbing". — FP-1747
- Franklin admits he is baffled by the jar: "So wonderfully are these two States of Electricity, the plus and minus combined and ballanced in this miraculous Bottle! situated and related to each other in a Manner that I can by no Means comprehend!" — FP-Jul1747
- **Why current "flows the wrong way" (explanation, our wording):** Franklin guessed that rubbed glass *gains* electric fire and called that "plus". Every diagram since draws current from plus to minus. In 1897 the particle that actually moves in a wire turned out to carry the "minus" charge (section 5), so in wires the electrons drift against Franklin's arrow. Franklin had a 50/50 guess and lost the coin toss. — FP-1747; APS-ELEC; HP-CUR
- **Franklin's turkey (Christmas 1750):** "I have lately made an Experiment in Electricity that I desire never to repeat." — FP-Turkey
- He was "about to kill a Turkey by the Shock from two large Glass Jarrs containing as much electrical fire as forty common Phials", and shocked himself instead: "the flash was very great and the crack as loud as a Pistol; yet my Senses being instantly gone, I neither Saw the one nor heard the other". — FP-Turkey
- "do not make it more Publick, for I am Ashamed to have been Guilty of so Notorious A Blunder". — FP-Turkey

## 3. Fire From the Sky (Marly, the kite, lightning rods, Richmann)

- Dalibard's memoir was read to the Académie Royale des Sciences on 13 May 1752. — FP-Dalibard
- At Marly-la-Ville, "situé à six lieuës de Paris", he set up an iron rod "d'environ un pouce de diamètre, longue de quarante pieds et fort pointuë" [about an inch thick, forty feet long, very sharp]. — FP-Dalibard
- It stood on "une petite planche quarrée portée sur trois bouteilles à vin" [a small square board on three wine bottles]. — FP-Dalibard
- Dalibard was away. The watch was kept by Coiffier, "qui a servi quatorze ans dans les dragons" [who had served fourteen years in the dragoons]. — FP-Dalibard
- "Le Mercredi 10. Mai 1752. entre deux et trois heures après midi" [Wednesday 10 May 1752, between two and three in the afternoon] Coiffier heard thunder, ran to the rod, and drew "une petite étincelle brillante" [a small bright spark]. — FP-Dalibard
- He sent for the Prior. Seeing their priest run, the villagers "s'imaginent que le pauvre Coiffier a été tué du tonnerre" [imagined poor Coiffier had been killed by thunder]. And "la grêle qui survient n'empêche point le troupeau de suivre son Pasteur" [the hail did not stop the flock from following their shepherd]. — FP-Dalibard
- Prior Raulet drew sparks too and later found a bruise round his arm "semblable à celle que feroit un coup de fil-d'archal" [like the lash of a wire]. — FP-Dalibard
- APS: "Franklin wasn't the first to successfully conduct this pivotal experiment." (APS gives 50 ft "in Paris"; the primary report says 40 French feet at Marly.) — APS-1752
- **The kite, in Franklin's words** (*Pennsylvania Gazette*, 19 Oct 1752): "it may be agreeable to the Curious to be inform'd, that the same Experiment has succeeded in Philadelphia, tho' made in a different and more easy Manner, which any one may try, as follows." — FP-Kite
- "Make a small Cross of two light Strips of Cedar, the Arms so long as to reach to the four Corners of a large thin Silk Handkerchief when extended". — FP-Kite
- Silk, because it "is fitter to bear the Wet and Wind of a Thunder Gust without tearing." — FP-Kite
- "As soon as any of the Thunder Clouds come over the Kite, the pointed Wire will draw the Electric Fire from them, and the Kite, with all the Twine, will be electrified, and the loose Filaments of the Twine will stand out every Way, and be attracted by an approaching Finger." — FP-Kite (also reproduced on FI)
- The holder "must stand within a Door, or Window, or under some Cover, so that the Silk Ribbon may not be wet". — FP-Kite
- "you will find it stream out plentifully from the Key on the Approach of your Knuckle. At this Key the Phial may be charg'd". — FP-Kite
- Priestley's 1767 account: Franklin was waiting for a spire to be built in Philadelphia, then thought of a kite. "But dreading the ridicule which too commonly attends unsuccessful attempts in science, he communicated his intended experiment to no body but his son, who assisted him in raising the kite." — FP-Priestley
- "One very promising cloud had passed over it without any effect". Then he saw "some loose threads of the hempen string to stand erect, and to avoid one another". — FP-Priestley
- "He perceived a very evident electric spark." — FP-Priestley
- "This happened in June 1752, a month after the electricians in France had verified the same theory, but before he heard of any thing they had done." — FP-Priestley
- Priestley called it "the greatest, perhaps, that has been made in the whole compass of philosophy, since the time of Sir Isaac Newton". — FP-Priestley
- William Franklin was 21 at the time, but paintings often show a boy. — Ars
- Franklin's own letter "never confirmed in the text whether the experiment was performed". — Ars (summarising B. A. Moura)
- Tom Tucker's *Bolt of Fate* (2003) "Argues that Franklin's kite experiment never took place and that it was a scientific hoax". — Tucker **UNCERTAIN (minority view; cite as a doubt, not a finding)**
- Franklin's interest began in 1743 after a show by the travelling lecturer Archibald Spencer. — Ars
- In 1753 Franklin received the Royal Society's Copley Medal for his "curious experiments and observations on electricity." — FI
- **Lightning rods** (*Poor Richard Improved*, 1753): "Provide a small Iron Rod… of such a Length, that one End being three or four Feet in the moist Ground, the other may be six or eight Feet above the highest Part of the Building." — FP-PoorRichard
- "To the upper End of the Rod fasten about a Foot of Brass Wire, the Size of a common Knitting-needle, sharpened to a fine Point". — FP-PoorRichard
- "A House thus furnished will not be damaged by Lightning, it being attracted by the Points, and passing thro the Metal into the Ground without hurting any Thing." — FP-PoorRichard
- Why tall pointed things get hit: "Height, pointy shape, and isolation are the dominant factors controlling where a lightning bolt will strike." — NWS-Myths
- **Richmann (St Petersburg):** Professor Richmann "was struck dead, on the 6th of August 1753, by a flash of lightning drawn by his apparatus into his own room". — Priestley1775 **UNCERTAIN (Old Style/New Style date not checked)**
- His engraver companion Sokolow "observed a globe of blue fire, as he called it, as big as his fist, jump from the rod". It came with "a report as loud as that of a pistol", and "the door torn off, and thrown into the room". — Priestley1775 (keep this brief and gentle in narration)

## 4. Frogs and the Pile (Coulomb, Galvani, Volta, Napoleon, Frankenstein)

- Coulomb was born on 14 June 1736 at Angoulême and served as a military engineer. — Coulomb (editor's biography)
- His law (1785): "La force répulsive de deux petits globes électrisés de la même nature d'électricité est en raison inverse du carré de la distance du centre des deux globes." [The repulsion between two small charged balls of the same kind falls off as the square of the distance between their centres.] — Coulomb
- His torsion balance hung from a fine silver wire 28 *pouces* (inches) long. — Coulomb
- His trial numbers: balls 36° apart under 36° of twist; 18° apart needing 144°; about 8.5° apart needing 576°. "à la moitié de la première distance, la répulsion des balles est quadruple" [at half the distance, the repulsion is four times as great]. — Coulomb
- Galvani's manuscripts record an experiment with an electrical machine dated 6 Nov 1780, "but this was not the first observation made by Galvani". — Galvani (translator's intro)
- *De viribus* appeared in the Bologna Academy's *Commentarii* vol. VII, in an issue dated 27 March 1791. Its author was "the 54 year old Professor of Obstetrics at the Institute." — Galvani (preface)
- The chance discovery: "When by chance one of those who were assisting me gently touched the point of a scalpel to the medial nerves… immediately all the muscles of the limbs seemed to be so contracted that they appeared to have fallen into violent tonic convulsions", whenever a spark was drawn from a machine nearby. — Galvani
- "Hereupon I was fired with incredible zeal and desire of having the same experience". — Galvani
- From his September 1786 notes: "on an evening early in September 1786, we placed some frogs horizontally on a parapet, prepared in the usual manner by piercing and suspending their spinal cords with iron hooks." — Galvani (translator's intro, quoting the manuscripts)
- Galvani believed animal tissue had its own electricity, and Volta "strongly opposed" him. (Modern nerve science shows both were partly right. See section 18.) — Piccolino
- Galvani lost his post "when he refused to take the oath of allegiance required by the occupying Napoleonic army", and died in 1798. — ETHW-Galvani
- **Volta's letter:** headed "A Côme en Milanois, ce 20me Mars, 1800", written in French to Sir Joseph Banks, President of the Royal Society, and "Read June 26, 1800". — Volta1800
- "Oui, l'appareil dont je vous parle, et qui vous étonnera sans doute, n'est que l'assemblage d'un nombre de bons conducteurs de différente espèce, arrangés d'une certaine manière." [Yes, the apparatus I speak of, which will doubtless astonish you, is only an assembly of a number of good conductors of different kinds, arranged in a certain way.] — Volta1800
- "30, 40, 60 pièces, ou d'avantage, de cuivre, ou mieux d'argent" [30, 40, 60 pieces or more, of copper or better silver], each paired with tin or zinc and separated by wet card. — Volta1800
- The Royal Society abstract: a silver disc "(half-a-crown, for instance,)", then zinc, then soaked pasteboard or leather, "repeated thirty or forty times, forming thus what the author calls his columnar machine." — VoltaAbstract
- It had "the singular property of acting without intermission, or rather of re-charging itself continually". — VoltaAbstract
- Volta: "Cette circulation sans fin du fluide électrique, (ce mouvement perpétuel,) peut paroitre paradoxe… mais elle n'en est pas moins vraie et réelle, et on la touche, pour ainsi dire, des mains." [This endless circulation of the electric fluid may seem a paradox… but it is no less true and real, and one touches it, so to speak, with one's hands.] — Volta1800
- He called it the "Organe électrique artificiel" [artificial electric organ], after the torpedo fish. — Volta1800
- Volta's original piles "were destroyed in a fire in Como in 1899". Copies are at Pavia, where he taught experimental physics from 1778. — Pavia
- The volt is named after him. — ETHW-Volta
- At Napoleon's invitation Volta demonstrated in Paris: "Le premier consul voulut assister en personne à la séance" [the First Consul wished to attend in person]. A gold medal was voted "par acclamation". — Arago **UNCERTAIN (year; usually given as 1801, but the scan is garbled)**
- At Institut sessions Napoleon would ask: "Où est Volta? serait-il malade? pourquoi n'est-il pas venu?" [Where is Volta? Is he ill? Why hasn't he come?] — Arago
- Napoleon gave him the Legion of Honour, the Iron Crown and "la dignité de comte". — Arago (year of the countship **UNCERTAIN**: ETHW says 1801, others 1810)
- Aldini, Galvani's nephew, published *An account of the late improvements in Galvanism* (London, 1803). — Aber; Newgate
- After a hanging at Newgate in January 1803, the body "was subjected to the galvanic process by Professor Aldini". — Newgate
- "Some of the uninformed bystanders thought that the wretched man was on the eve of being restored to life. This, however, was impossible". — Newgate (keep any narration gentle; leave out the grisly detail)
- Mary Shelley, 1831, recalling the summer of 1816: "Perhaps a corpse would be re-animated; galvanism had given token of such things". — Shelley1831
- Then: "When I placed my head on my pillow, I did not sleep, nor could I be said to think." — Shelley1831

## 5. What Is It, Actually? (Thomson, Millikan, the 2019 redefinition)

- The discovery of the electron "was announced during the course of his evening lecture to the Royal Institution on Friday, April 30, 1897." — NOBEL-JJT-BIO
- In 1897 Thomson "showed that cathode rays ... consist of particles— electrons—that conduct electricity. Thomson also concluded that electrons are part of atoms." — NOBEL-JJT
- Thomson: "I can see no escape from the conclusion that (cathode rays) are charges of negative electricity carried by particles of matter." — APS-ELEC
- Their mass-to-charge ratio "turned out to be over one thousand times smaller than that of a charged hydrogen atom." — APS-ELEC
- In the lecture he said "corpuscles" throughout, "never mentioning the word electron". — RI-JJT
- "Electron" was "coined in 1891 by G. Johnstone Stoney". It was "Irish physicist George Francis Fitzgerald who suggested in 1897 that the term be applied to Thomson's corpuscles." — APS-ELEC
- Thomson concluded "that all matter, whatever its source, contains particles of the same kind that are much less massive than the atoms of which they form a part." — BRIT-JJT
- A distinguished listener "admitted years later that he believed Thomson had been 'pulling their legs.'" — APS-ELEC
- Nobel Prize in Physics 1906 to Thomson, "in recognition of the great merits of his theoretical and experimental investigations on the conduction of electricity by gases". — NOBEL-JJT
- Thomson was knighted in 1908. His son George Paget Thomson won the Physics Nobel in 1937. — NOBEL-JJT-BIO
- Millikan's 1923 Nobel was "for his work on the elementary charge of electricity and on the photoelectric effect". — NOBEL-MIL
- "Small electrically charged drops of oil were suspended between two metal plates where they were subjected to the downward force of gravity and the upward attraction of an electrical field." — NOBEL-MIL
- Water droplets evaporated too fast. Graduate student Harvey Fletcher "found that he could use droplets of oil, produced with a simple perfume atomizer." — APS-MIL
- Millikan's Nobel lecture opens: "Science walks forward on two feet, namely theory and experiment". — MIL-LECT
- His 1913 value, "1.592 x 10-19 coulombs, is slightly lower than the currently accepted value of 1.602 x 10-19 C, probably because Millikan used an incorrect value for the viscosity of air." — APS-MIL (DERIVED: about 0.6% low)
- His notebooks have margin notes like "beauty publish" and "something wrong". Some historians have called this fraud; others see "striving for accuracy". — APS-MIL
- "Starting on May 20, 2019, the ampere is based on a fundamental physical constant: the elementary charge (e)". — NIST-AMP
- The old ampere was defined by the force between two wires "of infinite length", and so "could not be physically realized according to its own definition". — NIST-AMP

## 6. Pressure, Flow and Friction (voltage, current, resistance; Ohm)

- Voltage "is an expression of the available energy per unit charge which drives the electric current". In the water version, "the pressure P drives the water around the closed loop of pipe at a certain volume flowrate F." — HP-WATER
- "A battery is analogous to a pump in a water circuit." — HP-WATER
- A resistor is like "a severe constriction in a water pipe". — HP-WATER
- The analogy's limits: "All such analogies have their drawbacks". A reservoir picture "creates the mistaken impression that you can pull some charge out of it without putting some in." — HP-WATER
- Faraday "was not convinced that electricity was a material fluid that flowed through wires like water through a pipe." — BRIT-FAR
- Gentle analogy (our wording, consistent with HP-WATER): voltage is how hard the pump pushes, current is how much water passes each second, resistance is how narrow the pipe is. Ohm's law says that, for a given pipe, push twice as hard and twice as much flows.
- Georg Ohm's law appeared in "his pamphlet Die galvanische Kette, mathematisch bearbeitet (1827; The Galvanic Circuit Investigated Mathematically)". — BRIT-OHM
- "it was so coldly received that Ohm resigned his post at Cologne." — BRIT-OHM
- "Although Ohm's work strongly influenced theory, it was received with little enthusiasm. Ohm's feeling were hurt ... in March 1828, he formally resigned his position at Cologne." — MACTUTOR-OHM
- "He certainly did not find favour with Johannes Schultz who was an influential figure in the ministry of education in Berlin, and with Georg Friedrich Pohl, a professor of physics in that city." — MACTUTOR-OHM
- Part of the trouble was his own writing. Ohm "nowhere indicated precisely which of their several mathematical and verbal expressions he wished to be taken as the canonical form." — MACTUTOR-OHM (quoting historian K. Caneva)
- The famous "a web of naked fancies" insult is **UNCERTAIN (not found in any source we fetched)**.
- In 1841 the Royal Society of London gave him the Copley Medal, and made him a foreign member a year later. — BRIT-OHM; ETHW-OHM
- His father, a locksmith, was "an entirely self-taught man". As a student Ohm "spent much time dancing, ice skating and playing billiards". — MACTUTOR-OHM
- He got the Munich chair of physics only in 1852, "two years before his death". — MACTUTOR-OHM

## 7. The Slow Electrons (drift velocity vs the signal)

- OpenStax: the signal travels "on the order of 10^8 m/s, a significant fraction of the speed of light", while the charges themselves drift "on the order of 10^−4 m/s". — OSX-9.2
- The worked example: 12-gauge copper wire carrying 20.0 A gives a drift speed of "−4.54×10−4 m/s". "Household wiring often contains 12-gauge copper wire". — OSX-9.2
- The signal "moves on the order of 10^12 times faster (about 10^8 m/s) than the charges that carry it." — OSX-9.2
- **DERIVED:** at 4.54×10⁻⁴ m/s, an electron needs about 2,200 seconds, roughly 37 minutes, to drift one metre. That is at a circuit's full 20 A.
- **DERIVED (scaled from OSX-9.2, speed ∝ current/area):** a single 60 W bulb at 120 V draws about 0.5 A. In 14-gauge wire that is about 1.8×10⁻⁵ m/s, roughly fifteen hours per metre. A 9 W LED gives about four days per metre.
- HyperPhysics worked case: a 1 mm copper wire at 3 A, "the calculated drift velocity is just 0.00028 m/s. This would be more typical for working conditions in this wire." — HP-OHM
- "this drift velocity is on the order of millimeters per second in contrast to the speeds of the electrons themselves which are on the order of a million meters per second." — HP-OHM
- The electrons are not lazy: each one darts about very fast, but zig-zags. They "collide with atoms and other free electrons in the conductor. Thus, the electrons move in a zig-zag fashion and drift through the wire." — OSX-9.2
- "Even the electron speeds are themselves small compared to the speed of transmission of an electrical signal down a wire, which is on the order of the speed of light, 300 million meters per second." — HP-OHM
- **DERIVED:** on 60 Hz AC there is no net drift. Electrons rock back and forth by a tiny amount: for a 0.5 A lamp, about 70 nanometres, a few hundred atoms' widths.
- Why the light still comes on at once: "the electrons behave as an incompressible fluid. Thus, when a free charge is forced into a wire ... another leaves almost immediately, carrying the signal rapidly forward." — OSX-9.2
- "this fast-moving signal, or shock wave, is a rapidly propagating change in the electrical field due to equally rapid adjustments of surface charge." — OSX-9.2
- "Although your light turns on very quickly when you flip the switch, and you find it impossible to flip off the light and get in bed before the room goes dark, the actual drift velocity of electrons through copper wires is very slow. It is the change or 'signal' which propagates along wires at essentially the speed of light." — HP-DRIFT
- Feynman on a wire: "there is a Poynting vector directed radially inward ... There is a flow of energy into the wire all around. It is, of course, equal to the energy being lost in the wire in the form of heat." — FEYN-II-27
- "So our 'crazy' theory says that the electrons are getting their energy to generate heat because of the energy flowing into the wire from the field outside." — FEYN-II-27
- "Intuition would seem to tell us that the electrons get their energy from being pushed along the wire, so the energy should be flowing down (or up) along the wire. But the theory says that the electrons are really being pushed by an electric field, which has come from some charges very far away". — FEYN-II-27
- "The energy somehow flows from the distant charges into a wide area of space and then inward to the wire." — FEYN-II-27
- On a charging capacitor: "The energy isn't actually coming down the wires, but from the space surrounding the capacitor." — FEYN-II-27
- Feynman's reassurance: "You don't need to feel that you will be in great trouble if you forget once in a while that the energy in a wire is flowing into the wire from the outside, rather than along the wire." — FEYN-II-27
- "but it is clear that our ordinary intuitions are quite wrong." — FEYN-II-27
- On a two-wire line: "The wave travels down the line with the speed of light", provided there are "no dielectrics or magnetic materials in the space between the conductors". Real insulation slows it to a large fraction of light speed. — FEYN-II-24 (the exact 0.6–0.9c range is **UNCERTAIN**)

## 8. The Needle That Twitched (Ørsted, Ampère)

- "During a lecture demonstration, on April 21, 1820, while setting up his apparatus, Oersted noticed that when he turned on an electric current ... a compass needle held nearby deflected away from magnetic north". — APS-OER (Britannica and ETHW give only "April 1820")
- "The compass needle moved only slightly, so slightly that the audience didn't even notice." — APS-OER
- "He noted that the experiment made no strong impression on his audience." — ETHW-OER
- Accident or design? "accounts differ on whether the demonstration was designed to look for a connection between electricity and magnetism". — APS-OER
- "On July 21, 1820, Oersted published his results in a pamphlet, which was circulated privately to physicists and scientific societies." — APS-OER (that it was in Latin is **UNCERTAIN**, not on fetched pages)
- His battery "probably produced an emf of about 15-20 volts". The effect "couldn't be shielded by placing wood or glass between". — APS-OER
- Ørsted also made the first metallic aluminium (1825) and discovered piperine, the sharp taste in pepper (1820). — BRIT-ORS
- "Had Ampère died before 1820, his name and work would likely have been forgotten." His friend Arago demonstrated Ørsted's discovery to the French Academy. — BRIT-AMP
- "Ampère immediately set to work". He showed that "two parallel wires carrying electric currents repel or attract each other, depending on whether the currents flow in the same or opposite directions". — BRIT-AMP
- His 1827 *Mémoire* "coined the name of his new science, electrodynamics". — BRIT-AMP
- "an international convention signed in 1881 established the ampere as a standard unit of electrical measurement, along with the coulomb, volt, ohm, and watt". — BRIT-AMP

## 9. The Bookbinder (Michael Faraday)

- Born 22 September 1791, Newington, Surrey. "His father was a blacksmith". He remembered "being given one loaf of bread that had to last him for a week." — BRIT-FAR
- At 13 he became "a newspaper and errand boy by George Riebau". His schooling was "little more than the rudiments of reading, writing and arithmetic" (his own words). — RI-NOTEBOOKS
- "He served an apprenticeship with George Riebau as a bookbinder from 1805 to 1812." — RI-FARADAY
- He read the books he bound. "The article on electricity in the third edition of the Encyclopædia Britannica particularly fascinated him." — BRIT-FAR
- From 1810 he paid "one shilling per lecture" to hear John Tatum's science talks, 13 lectures in all. — RI-NOTEBOOKS
- His bound notes, "when shown to Riebau and a Patron of the shop in early 1812, led to him attending the last four lectures to be delivered by Humphry Davy". — RI-NOTEBOOKS (the patron's name, William Dance, is **UNCERTAIN**; the RI does not name him)
- "He sent a bound copy of his notes to Davy along with a letter asking for employment, but there was no opening ... when one of his laboratory assistants was dismissed for brawling, he offered Faraday a job." — BRIT-FAR
- "He was Assistant in the Royal Institution's laboratory for part of 1813". — RI-FARADAY (APS also gives 1813)
- "It has been said, with some truth, that Faraday was Davy's greatest discovery." — BRIT-FAR
- **The first motor:** "On Monday 3 September 1821, in the small Royal Institution basement laboratory lit by candlelight, a young Michael Faraday made a remarkable discovery: for the first time, continuous mechanical movement was generated from electricity". — RI-MOTOR
- His notebook that day: "In this way got the revolution of the wire round the pole of the magnet." And: "Very satisfactory, but make more sensible apparatus". — RI-MOTOR
- He sent "pocket-sized models of his device to scientific colleagues all over the world". — RI-MOTOR
- The RI's 1822 mercury-bath apparatus is "the first surviving electric motor". — RI-MOTOR-OBJ
- **Induction:** "He achieved success with the device pictured above on 29 August 1831." The wire was "made for bonnets", insulated with cotton. Winding it took "probably about ten working days". — RI-RING
- That ring, made "in August 1831", is "the first ever electric transformer." — RI-RING
- When he switched the current off, the needle kicked the other way: "he was astonished". — BRIT-FAR
- With a magnet pushed into a coil, "the needle of the galvanometer leapt into action". "Virtually all electric power is produced using Faraday's principles". — RI-GEN
- **Lines of force:** "the magnitude of a current was dependent upon the number of lines of force cut by the conductor in unit time." — BRIT-FAR
- In 1851 he fixed patterns of iron filings on waxed paper "by gently heating the waxed paper to set the iron filings on the page". You can still see the lines today. — RI-IRON
- He coined the words "electrode, cathode, ion (early 1830s)". — RI-FARADAY
- "Michael Faraday started the CHRISTMAS LECTURES® at the Ri in 1825", and "went on to present a total of 19 - the most by one individual ever!" — RI-XMAS
- They have run every year since, "stopping only for World War II". — RI-XMAS
- "his famous Chemical History of a Candle (1861) was edited and published by his friend William Crookes." — RI-FARADAY
- "He was twice offered the Presidency of the Royal Society, but declined on both occasions." — RI-FARADAY
- "He publicly stated several times that he would not accept a knighthood, but no evidence has been found that he was ever offered one." — RI-FARADAY
- The "tax it" story first appears in print in 1899, second-hand: "Gladstone's only commentary was 'but, after all, what use is it?'", and Faraday replies "there is every probability that you will soon be able to tax it!" — LECKY-1899 **UNCERTAIN (hearsay, printed 32 years after Faraday's death; no mention of electricity)**
- "What use is a newborn baby?": **UNCERTAIN / apocryphal for Faraday**. No Faraday source exists. The line is usually attributed to Franklin at a 1783 balloon launch, and even that is questioned (Chapin, *Proc. Amer. Philos. Soc.* 129:3, 1985).

## 10. Light Is Electricity Too (Maxwell, Hertz)

- Maxwell's first paper on the subject was "On Faraday's Lines of Force" (1855). — ETHW-MAX
- His field equations were "based on Michael Faraday's observations of the electric and magnetic lines of force". — BRIT-MAX
- In 1862 he computed the speed of his electric waves: "310,740,000,000 millimetres per second,=193,088 miles per second". Fizeau's measured speed of light was "195,647 miles per second". — MAXWELL-1862
- "we can scarcely avoid the inference that light consists in the transverse undulations of the same medium which is the cause of electric and magnetic phenomena." — MAXWELL-1862
- In 1865: "This velocity is so nearly that of light, that it seems we have strong reason to conclude that light itself (including radiant heat, and other radiations if any) is an electromagnetic disturbance in the form of waves propagated through the electromagnetic field according to electromagnetic laws." — MAXWELL-1865
- "Initially Maxwell wrote a set of twenty equations, which were incomprehensible to most of his contemporaries." Oliver Heaviside later boiled them down. — ETHW-MAX
- Einstein (1931) called the change Maxwell made "the most profound and the most fruitful that physics has experienced since the time of Newton." — BRIT-MAX
- Feynman: "From a long view of the history of mankind—seen from, say, ten thousand years from now—there can be little doubt that the most significant event of the 19th century will be judged as Maxwell's discovery of the laws of electrodynamics. The American Civil War will pale into provincial insignificance in comparison with this important scientific event of the same decade." — FEYN-II-1
- Near the end of his life Maxwell said: "I never had a violent shove in all my life." — ETHW-MAX (quoting Campbell 1882)
- Maxwell's ideas "were accepted by few outside England until 1886, when ... Hertz verified the existence of electromagnetic waves". — BRIT-EM
- "Between 1885 and 1889, while he was professor of physics at the Karlsruhe Polytechnic, he produced electromagnetic waves in the laboratory and measured their length and velocity." — BRIT-HERTZ
- Hertz showed that "rather than being instantaneous, electromagnetic effects propagate at a finite speed." — ETHW-HERTZ
- Hertz died on 1 January 1894, not yet 37. The hertz unit was set by the IEC in 1930. — ETHW-HERTZ
- Hertz's "It's of no use whatsoever" is **UNCERTAIN (widely repeated, no source found)**.

## 11. Light for the City (Edison's lamp, Holborn, Pearl Street)

- "Thomas Alva Edison did not invent the first light bulb". Earlier bulbs "burned out after a few minutes". "What Edison invented was the first incandescent light that was practical, that would light for hours and hours." — NPS-Light
- "In the fall of 1879, the muckers tested a small cotton thread as a filament. (Some books give the date as October 21, but new research has proven this to be false.) First they carbonized it, burning it to make it hard." — NPS-Light
- "The bulb burned at least 13 hours. (Some books say it burned even longer.)" — NPS-Light
- Charles Batchelor tested "Platinum, rubber, even the black soot from kerosene lamps". Later "Batchelor found an even better filament than the cotton thread--bamboo from Japan." — NPS-Light
- "Advancing on the work of Joseph Wilson Swan, an English physicist, Edison found that a carbon filament provided a good light with the concomitant high resistance required for subdivision." — Brit-Edison
- "beginning in the fall of 1878, Edison devoted thirty months to developing a complete system of incandescent electric lighting." — EdisonPapers-Bio
- That system included "the screw socket to hold his lamps in the fixtures and fuses to prevent electrical overloads and fires." — EdisonPapers-Light
- "Only in 1925 did half of all homes in the U.S. have electric power." — NPS-Light
- London first: Holborn Viaduct, "3,000 light capacity… the first central station for incandescent electric lighting established in the world (started up Jan. 12, 1882)." — ETHW-Hammer
- Holborn "was intended only as a temporary installation, so the Pearl Street station is often regarded as marking the beginning of electric-power distribution." — ETHW-EarlyApps
- IEEE Milestone: "On 4 September 1882, Edison's direct current (dc) generating station at 257 Pearl Street, began supplying electricity to customers in the First District, a one-quarter square mile (0.65 square km) area." — ETHW-Pearl
- "Edison was standing in the office of J. Pierpont Morgan of Drexel, Morgan & Company, one of his principal investors, when he gave the signal to John W. Lieb, chief electrician, to close the switch". — ETHW-Pearl
- "While the six dynamos could supply up to 7,200 lamps, there were only some 85 customers having a total of about 400 lamps on the first day of operation." — ETHW-Pearl
- It "grew to about 10,000 lamps serving 513 customers within a year." — ETHW-Pearl
- The 27-ton "Jumbo" dynamos were "named for a circus elephant then owned by P.T. Barnum". Each was about 100 kW, enough for "about 1,200 lamps". — ETHW-Pearl
- "The original system operated at 110 V dc." Underground cables were "insulated with beeswax, linseed oil, and asphaltum". — ETHW-Pearl
- The New York Times printed the news under "Miscellaneous City News". — ETHW-Pearl
- Pearl Street ran "from 4 September 1882 to 2 January 1890 with only one interruption, that lasting for three hours." — ETHW-Pearl
- Only "'old number nine,' a survivor of the 1890 fire, remains and is on display at the Henry Ford Museum". "The Pearl Street station site today is a public parking facility." — ETHW-Pearl
- DC's weakness: "high line losses that limit the distance that the dc electric power can be economically transmitted." — ETHW-Pearl

## 12. The War of the Currents (Stanley, Tesla, Westinghouse, Chicago, Niagara)

- Gaulard and Gibbs's AC system was "first demonstrated in 1881 in London". Westinghouse later "imported a set of Gaulard-Gibbs transformers and a Siemens AC generator". — Brit-Westinghouse
- "On 20 March 1886 William Stanley provided alternating current electrification to offices and stores on Main Street in Great Barrington, Massachusetts." — ETHW-Stanley
- Stanley stepped "up the 500-volt output of the Siemens generator to 3000-volts", then back down for the lamps. — ETHW-Stanley
- The wires were "fastened to the elm trees which lined that thoroughfare". "A total of twenty business establishments were then lighted". — ETHW-Stanley
- Stanley's key fixes: transformers "needed to be connected in parallel", and the magnetic core had to be "a closed circuit". — ETHW-Stanley
- AC won "because of the ability to efficiently adjust voltage levels… This was not possible in the direct current system because transformers do not work on 'D.C.'" — ETHW-Stanley
- The first US commercial AC central station was "placed in service in Buffalo on November 30, 1886". — ETHW-Buffalo
- Copper was so costly that at Montpelier, Vermont (1887), "the value of the copper salvaged was enough to cover the cost of conversion" from DC to AC. — ETHW-Buffalo
- Tesla "sailed for America in 1884, arriving in New York with four cents in his pocket, a few of his own poems, and calculations for a flying machine." — Brit-Tesla
- "In 1884, he went to New York and immediately took a job with Edison". — ETHW-Tesla
- In 1883 at Strassburg he "constructed, after work hours, his first induction motor." — Brit-Tesla
- US Patent 381,968, "Electro-magnetic motor": filed 12 Oct 1887, granted 1 May 1888. — Patent381968
- "On May 1, 1888 Nikola Tesla was issued his first set of patents for a comprehensive system of generators, transformers, synchronous motors and induction motors". — ETHW-Buffalo
- His lecture was "read before the American Institute of Electrical Engineers, in New York, in May, 1888, under the title 'A New System of Alternate Current Motors and Transformers.'" — Martin1894
- Westinghouse bought the patent rights in mid-1888: Britannica says "In May 1888"; ETHW says "Two months later" than the 1 May patents. — Brit-Tesla; ETHW-Buffalo
- Later, "Tesla supposedly tore up his contract and refused further royalties". — ETHW-Tesla **UNCERTAIN (ETHW's own "supposedly")**
- Edison "refused to develop an alternating current system due to his belief that high voltages were inherently unsafe, a view that was reinforced by his personal and financial investment in direct current technology." — EdisonPapers-Light
- "Edison's efforts to demonstrate the dangers of high current included experiments on the electrocution of animals and the development of the electric chair". — EdisonPapers-Light (mention lightly, without detail)
- On 6 August 1890 New York carried out its first electric-chair execution at Auburn. "Dc proponents said the condemned murderer had been 'Westinghoused.'" — Brit-Electrocution; ETHW-Buffalo (keep to one line in a sleep script)
- "By the time Edison's company forced him to develop an alternating current system in 1891, it was too late, and in February 1892, the Edison company was merged into General Electric, and Edison left the industry he had helped to found." — EdisonPapers-Light
- Chicago 1893: Westinghouse won the lighting contract "by bidding about one-third of the bid submitted by the recently formed General Electric Company", then built "a quarter million" of his own "stopper" lamps in under a year to avoid Edison's patents. — ETHW-Buffalo
- "The Exhibition used more electricity than the whole City of Chicago." — ETHW-Buffalo
- "U.S. Pres. Grover Cleveland pushed a button… turning on the electric power for the exposition", the "White City, electrically lighted at night". — Brit-Columbian
- Total attendance "was more than 25.8 million". — Brit-Columbian
- **Niagara, 1895:** "When the Adams Plant went into operation on August 26, 1895, it represented a key victory for alternating-current systems over direct-current." — ETHW-Adams
- It reached "its full capacity of ten 5,000-HP generators in May 1900". — ETHW-Adams
- Niagara chose 25 Hz, after tests had "shown that at 25 Hz incandescent lamps did not show objectionable flickering." — ETHW-Buffalo
- **Buffalo, 1896:** an 11,000-volt, "22-mile transmission line" on "cedar wood poles". "Service was inaugurated November 15, 1896. Overall efficiency was 79.6%." — ETHW-Buffalo
- Buffalo's 25 Hz system lasted more than a century, until "the elimination of the 25-Hz system by December 31, 2007". — ETHW-Buffalo
- The Topsy myth and the $50,000 story: see Corrections. — Smithsonian-Topsy; Tesla-MyInventions
- From Tesla's 1919 memoir, Edison's praise: "I have had many hard-working assistants but you take the cake." — Tesla-MyInventions **UNCERTAIN (Tesla's own recollection)**

## 13. The Quiet Box on the Pole (transformers and transmission)

- Faraday's 1831 ring was "the first ever electric transformer." — RI-RING
- How it works (our wording): two coils share an iron core. A changing current in the first coil makes a changing magnetic field, and that induces a voltage in the second. More turns on the second coil gives more voltage; fewer turns gives less. It only works while the current keeps changing, which is why transformers "do not work on 'D.C.'" — ETHW-Stanley
- Transformers "either increase (step up) or reduce (step down) voltages". — EIA-Delivery
- "Higher-voltage electricity makes long-distance electricity transmission more efficient and less expensive." — EIA-Delivery
- "Operating the transmission lines at high voltage (i.e., 230,000 to 765,000 volts) reduces the losses of electricity from conductor heating and allows power to be shipped economically over long distances." — TaskForce2003
- Why (our wording): heat lost in a wire grows with the *square* of the current. Double the voltage and you can send the same power with half the current, which cuts the heating to about a quarter. — consistent with TaskForce2003
- US "transmission and distribution (T&D) losses averaged about 5% of the electricity transmitted and distributed in the United States in 2018 through 2022." — EIA-Losses

## 14. The Grid That Balances Every Second

- "electricity flows at close to the speed of light… and is not economically storable in large quantities. Therefore electricity must be produced the instant it is used." — TaskForce2003
- "if there is more load than generation at any moment, frequency drops below 60 Hz, and it rises above that level if there is more generation than load." — TaskForce2003
- "Grid frequency is a measure of the health of the grid, as it reflects the ability of a grid to balance supply and demand." — NREL-Inertia
- "In the grid, inertia refers to the kinetic energy stored in spinning generators." — NREL-Inertia
- "On a bicycle, inertia gives the rider a chance to stop pedaling and coast without falling over. In the grid, it gives the system operator a chance to respond to power plant failures". — NREL-Inertia
- Inertia "is typically available for a few seconds". — NREL-Inertia
- The flyball governor: "If the grid frequency falls, the balls slow down and retract… allowing more steam into the turbine." NREL calls it "the cruise control for the power grid." — NREL-Inertia
- A balancing authority "ensures, in real time, that power system demand and supply are finely balanced." — EIA-2016
- Mains clocks keep time by counting cycles: "Time error is caused by a deviation in Interconnection frequency from 60.0 Hertz", and "Time Error Correction" exists "to correct for the time error accumulated on electric clocks." — TaskForce2003
- **Why 60 Hz?** For Tesla's motor it was "necessary to reduce the alternations from 133 Hz. or cycles per second… to 60 Hz. This remains the standard North American frequency." — ETHW-Buffalo (why Europe settled on 50 Hz is **UNCERTAIN**, no source fetched)
- **The European clocks (2018):** the Continental grid "is experiencing a continuous system frequency deviation from the mean value of 50 Hz, and this since mid of January 2018." — ENTSOE-2018
- "The power deviations are originating from the control area called Serbia, Macedonia, Montenegro (SMM block) and specifically Kosovo and Serbia." "The missing energy amounts currently to 113 GWh." — ENTSOE-2018
- "These types of electric clocks show now a delay around six minutes." They are "typically radio-, oven clocks or clocks for programming the heating system." — ENTSOE-2018
- "The average frequency of the period since mid-January 2018 until today was around 49.996 Hz." — ENTSOE-2018
- "The political disagreements opposing the Serbian and Kosovar authorities have led to the observed electricity impact." — ENTSOE-2018
- "For the system to properly function the frequency cannot go below 47.6 and above 52.4 Hz." — ENTSOE-2018
- **The British kettle surge:** big TV events "often produce a surge in electricity demand during natural breaks as people make a cup of tea, open the fridge and flush the loo at the same time." — NESO-Euro2020
- The record: "1990 England vs Germany football world cup semi final 2800MW at the end of the penalty shoot-out". Others: "2011 Royal Wedding… 760MW"; "1966… 600MW after Geoff Hurst's iconic final goal". — NESO-Euro2020
- After the Queen's April 2020 address: "a 500-600MW pickup, the equivalent of 300,000 kettles all being boiled the same time!" — ESO-Lockdown
- Pumped-storage hydro helps, "with their reservoirs able to drain quickly". — NESO-Euro2020
- **Size of the US grid (2016):** "more than 7,300 power plants, nearly 160,000 miles of high-voltage power lines, and millions of low-voltage power lines and distribution transformers, which connect 145 million customers." — EIA-2016
- "At the beginning of the 20th century, more than 4,000 isolated electric utilities operated in the United States." — EIA-Delivery
- Three US grids: Eastern, Western and ERCOT (Texas). They "are electrically independent from each other except for a few small direct current (DC) ties that link them." — EIA-Delivery; TaskForce2003
- As of March 2026 the US had "57 nuclear power plants… with 96 reactors". — EIA-Plants
- World: "Global electricity demand rose by 4.3% in 2024", and the expected growth "corresponds to adding more than the equivalent of a Japan to the world's electricity consumption each year." — IEA-2025
- "Worldwide electricity demand grew by 3% year-on-year in 2025." — IEA-2026
- "Globally, solar PV generation hit the 2 000 TWh mark in 2024, producing 7% of global electricity generation". — IEA-2025

## 15. When the Lights Go Out (1965, 2003, 2025)

- **9 November 1965:** "This disturbance resulted in the loss of over 20,000 MW of load and affected 30 million people… Outages lasted for up to 13 hours." — TaskForce2003
- "A backup protective relay operated to open one of five 230-kV lines taking power north from a generating plant in Ontario to the Toronto area. When the flows redistributed instantaneously on the remaining four lines, they tripped out successively in a total of 2.5 seconds." — TaskForce2003
- The relay tripped "when the loading on the line exceeded the 375-MW relay setting", and "Operating personnel were not aware of the operating set point of this relay." — TaskForce2003 (the plant is named only as "Beck"; "Sir Adam Beck No. 2" is **UNCERTAIN**)
- NERC "was established in 1968, as a result of the Northeast blackout in 1965." — TaskForce2003
- No baby boom: "no increase in births associated with the blackout." — Udry1970
- **14 August 2003:** "The outage affected an area with an estimated 50 million people and 61,800 megawatts (MW) of electric load". — TaskForce2003
- "The blackout began a few minutes after 4:00 pm Eastern Daylight Time… and power was not restored for 4 days in some parts of the United States." — TaskForce2003
- "14:14 EDT: FE alarm and logging software failed. Neither FE's control room operators nor FE's IT EMS support personnel were aware of the alarm failure." — TaskForce2003
- "After 15:05 EDT, some of FE's 345-kV transmission lines began tripping out because the lines were contacting overgrown trees within the lines' right-of-way areas." — TaskForce2003
- "By 16:13 EDT, more than 508 generating units at 265 power plants had been lost". — TaskForce2003
- "Most of the event sequence, in fact, occurred in the final 12 seconds of the cascade." — TaskForce2003
- US cost "between $4 billion and $10 billion". — TaskForce2003
- "The report makes clear that this blackout could have been prevented". — TaskForce2003
- **28 April 2025:** "On 28 April 2025, at 12:33 CEST, the power systems of continental Spain and Portugal experienced a total blackout." — ENTSOE-IbPage
- "This was the most severe blackout on the European power system in over 20 years, and the first ever of its kind (overvoltage)." — ENTSOE-IbBrief
- The cause: "a combination of many interacting factors, including oscillations, gaps in voltage and reactive power control, differences in voltage regulation practices, rapid output reductions and generator disconnections in Spain, and uneven stabilisation capabilities. These factors led to fast increases of voltage and cascading generation disconnections". — ENTSOE-IbPage
- Automatic load-shedding schemes "were activated in Spain and Portugal but unable to stop the blackout due to its overvoltage nature". — ENTSOE-IbBrief
- "The system restoration was completed by 00:22 on 29 April 2025 in Portugal, and by 04:00 on the same day, the transmission system was restored in Spain." — ENTSOE-IbFactual
- "the Spanish system was fully restored within 16 hours, while the Portuguese system was back online within 12 hours". — ENTSOE-IbFinal
- Hydro plants and the links to France and Morocco helped restart the grid. — ENTSOE-0428
- A 49-member expert panel investigated it: factual report 3 Oct 2025, final report 20 Mar 2026. — ENTSOE-IbPage
- The Spanish government's own report (June 2025) is titled "Report from the Committee for the analysis of the electricity crisis of April 28th 2025". — ENTSOE-0619
- How many people lost power in Iberia (often quoted as 55–60 million) is **UNCERTAIN (not stated in the ENTSO-E reports read)**.

## 16. Lightning

- "nearly 1.4 billion flashes occur annually over the entire Earth. This annual flash count translates to an average of 44 ± 5 lightning flashes (intracloud and cloud‐to‐ground combined) occurring around the globe every second". — Christian2003
- That replaced an older guess: it "is well below the traditional estimate of 100 fl s−1 that was derived in 1925 from world thunder day records." — Christian2003
- It changes with the seasons: "a maximum of 55 fl s–1 in the boreal summer and a minimum of 35 fl s–1 in the austral summer". — Albrecht2016
- The count came from orbit: the Optical Transient Detector was launched "into a 70° inclination low Earth orbit in April 1995". — Christian2003
- Lightning prefers land, "with an average land/ocean ratio of ∼10:1." — Christian2003
- "There are roughly 5 to 10 times as many flashes that remain in the cloud as there are flashes which travel to the ground". — NSSL-Types
- "lightning can heat the air it passes through to 50,000 degrees Fahrenheit (5 times hotter than the surface of the sun)." (DERIVED: roughly 28,000 K, often rounded to 30,000 K.) — NWS-Temp
- "lightning is the movement of electrical charges and doesn't have a temperature; however, resistance to the movement of these electrical charges causes the materials that the lightning is passing through to heat up." — NWS-Temp
- "A typical lightning flash is about 300 million Volts and about 30,000 Amps. In comparison, household current is 120 Volts and 15 Amps." — NWS-Power
- NSSL's range: "Lightning can have 100 million to 1 billion volts, and contains billions of watts." — NSSL-FAQ
- "The actual diameter of the lightning channel current is one to two inches". — NSSL-Types
- How charge separates: "The lighter ice crystals become positively charged and are carried upward into the upper part of the storm by rising air." "The heavier hail becomes negatively charged". — NWS-Overview
- "when the differences in charges becomes too great, this insulating capacity of the air breaks down and there is a rapid discharge of electricity that we know as lightning." — NWS-Overview
- Even now: "(The actual breakdown process is still poorly understood.)" — NSSL-FAQ
- The stepped leader zigzags down "in roughly 50-yard segments" and is "invisible to the human eye". — NSSL-Types
- "Cloud-to-ground (CG) lightning comes from the sky down, but the part you see comes from the ground up." — NSSL-FAQ
- The return stroke "travels about 60,000 miles per second back towards the cloud." — NSSL-Types
- "We see lightning flicker when the process rapidly repeats itself several times along the same path." — NSSL-Types
- Thunder: lightning heats the air "to above 50,000° F in only a few millionths of a second!" — NSSL-FAQ
- "The disturbance is a shock wave for the first 10 yards, after which it becomes an ordinary sound wave, or thunder." — NSSL-FAQ
- Why it rumbles: "what you hear as thunder is actually an accumulation of multiple sound waves from the different portions of the lightning channel." — NSSL-FAQ
- Counting: divide the seconds between flash and thunder by 5 to get miles. "Normally, you can hear thunder about 10 miles from a lightning strike." — NWS-Overview
- Lightning also happens in "volcanic eruptions, extremely intense forest fires… heavy snowstorms, in large hurricanes". — NSSL-FAQ
- "In snowstorms, where it is somewhat rare, pink and green are often described as colors of lightning." — NSSL-FAQ
- It can fuse sand into "a glassy rock (called a fulgurite) in the shape of a convoluted tube." — NSSL-FAQ
- **Earth's lightning capital:** "directly over Lake Maracaibo in Venezuela… where 233 fl km–2 yr–1 occur". — Albrecht2016
- Storms form there "297 days per year on average", mostly at night. — Albrecht2016
- "Nocturnal thunderstorms over Lake Maracaibo are so frequent that their lightning activity was used as a lighthouse by Caribbean navigators in colonial times". — Albrecht2016
- They are called "the 'Lighthouse of Catatumbo,' the 'Never-Ending Storm of Catatumbo,' or simply Catatumbo lightning." — Albrecht2016
- Lope de Vega's poem *La Dragontea* (1598) credits them with stopping an English pirate's attack on Maracaibo. — Albrecht2016
- "The Empire State Building is hit an average of 23 times a year". — NWS-Myths
- "The human body does not store electricity. It is perfectly safe to touch a lightning victim to give them first aid." — NWS-Myths
- In a car, protection comes from "the outer metal shell of hard-topped metal vehicles... with the windows closed", not the tyres. — NWS-Cars

## 17. Above the Storms (sprites, elves, blue jets, Earth's circuit, aurora)

- Sprites appear "some 50 miles above Earth" and "flash for a scant one thousandth of a second." — NASA-Sprites
- "pilots had claimed to see them for almost a century before scientists at the University of Minnesota accidentally caught one on camera in July of 1989." — NASA-Sprites
- The first report used "a low-light-level television camera". The discharge it caught was "250 kilometers from the observing site". — Franz1990
- "On April 30, 2012, astronauts on the ISS captured the signature red flash of a sprite". — NASA-Sprites
- We rarely see them because "they emit most of their light in red, where the human eye is relatively blind." — NASA-Sprites
- Their shapes are "described as resembling jellyfish, carrots, or columns." — NSSL-Types
- "their root cause remains unknown. Some thunderstorms have them -- most don't." — APOD-Sprite
- Elves "are rapidly expanding disk-shaped regions of glowing that can be up to 300 miles across. They last less than a thousandth of a second". — NSSL-Types
- "Elves were discovered in 1992 by a low-light video camera on the Space Shuttle". — NSSL-Types
- Blue jets "extend up in narrow cones fanning out and disappearing at heights of 25-35 miles." — NSSL-Types
- Storms even make gamma rays: these flashes were found by satellites built for cosmic gamma rays, "but it was found that some signals were coming from thunderstorms on earth!" — NSSL-Types
- ESA's ASIM "is installed outside the European space laboratory Columbus to monitor electric events at high altitudes." — ESA-ASIM
- "In 2015 ESA astronaut Andreas Mogensen managed to record many kilometre-wide blue flashes around 18 km altitude, including a pulsating blue jet reaching 40 km", filmed "as he flew over the Bay of Bengal at 28 800 km/h". — ESA-ASIM
- **Earth's battery:** "Thunderstorms and electrified clouds are like batteries that cause the Earth to have negative charge and the atmosphere to have positive charge.. This maintains the fair weather electric field, which is about 100 V/m near the surface." — NSSL-FAQ
- "Without thunderstorms and lightning, the earth-atmosphere electrical balance would disappear in 5 minutes." — NSSL-FAQ
- "At any given moment about 2,000 thunderstorms roll over Earth". — NASA-SVS-Schumann
- Lightning's radio waves, trapped between the ground and "a boundary about 60 miles up", make "a repeating atmospheric heartbeat known as Schumann resonance", "as low as 8 Hertz". — NASA-SVS-Schumann (the precise "7.83 Hz" is **UNCERTAIN**)
- Aurora: "the result of electrons colliding with the upper reaches of Earth's atmosphere." "This is similar to how a neon light works. The aurora typically forms 80 to 500 km above Earth's surface." — NOAA-SWPC-Aurora
- "Late in the evening, near midnight, the arcs often begin to twist and sway, just as if a wind were blowing on the curtains of light." — NOAA-SWPC-Aurora
- "These diffuse patches often blink on and off repeatedly for hours, then they disappear as the sun rises in the east." — NOAA-SWPC-Aurora

## 18. The Body Electric (nerves, heart, brain)

- "the difference in charge is measured at -70 mV, the value described as the resting membrane potential." — OS-AP-12.4
- "All action potentials peak at the same voltage (+30 mV), so one action potential is not bigger than another." — OS-AP-12.4
- The change from -70 to +30 mV "is a 100 mV change", and the spike lasts "approximately 2 milliseconds". — OS-AP-12.4
- Across a membrane "only 8-nm-thick", that small voltage makes a field that "is immense (on the order of 11 MV/m!)". — OS-Phys-20.7
- Insulated nerves are faster because "the action potential basically jumps from one node to the next (saltare = 'to leap')". — OS-AP-12.4
- Nerve fibres "conduct such impulses at a speed of up to 120 m/s depending on their types." — Sonawane2023
- Hursh (1939) found "about 120 m/s (about 430 km/H) for an axon with a diameter of 20 μm". — Tsubo2024
- On uninsulated membrane the impulse "moves slowly (about 1 m/s)". — OS-Phys-20.7
- Hodgkin, Huxley and Eccles shared the 1963 Nobel "for their discoveries concerning the ionic mechanisms involved in excitation and inhibition in the peripheral and central portions of the nerve cell membrane". — Nobel1963
- They "turned to giant nerve fibres in the squid, which are almost a thousand times thicker than their human counterparts." — Nobel1963-Speed
- They "were surprised to find that the polarity did not drop from negative to zero during the transmission of an impulse as predicted, but in fact reversed, becoming electrically positive." — Nobel1963-Speed
- "The nervous system behaves like a series of microscopic generators". — Nobel1963-Speed
- Note: nerve signals are carried by ions (sodium, potassium) crossing membranes, not by electrons flowing down a wire. That is our gloss on OS-AP-12.4. Galvani's "animal electricity" was real, though not in the form he imagined.
- "The SA node has the highest inherent rate of depolarization and is known as the pacemaker of the heart." — OS-AP-19.2
- "The SA node, without nervous or endocrine control, would initiate a heart impulse approximately 80–100 times per minute." — OS-AP-19.2
- The backup: "Without the SA node, the AV node would generate a heart rate of 40–60 beats per minute." — OS-AP-19.2
- Einthoven won the 1924 Nobel "for his discovery of the mechanism of the electrocardiogram". — Nobel1924
- The ECG is "a record of the electrical potential fluctuations at the surface of the body, which accompany the heart beat." His string galvanometer used "a fine, silver-plated quartz wire". — Nobel1924-Speech
- "the human nervous system runs on roughly 20 watts, the same power demand as a couple of standard LED bulbs". — Ornes2025

## 19. The Electric Eel (Humboldt's horses, Catania)

- In March 1800, on the Venezuelan plains, Humboldt's guides proposed to "fish with horses". They "set off on the 19th of March, at a very early hour, for the village of Rastro". — Humboldt-PN2
- "They brought about thirty with them, which they forced to enter the pool." — Humboldt-PN2
- "These yellowish and livid eels, resembling large aquatic serpents, swim on the surface of the water, and crowd under the bellies of the horses and mules." — Humboldt-PN2
- "In less than five minutes two of our horses were drowned." Humboldt thought they were "probably not killed, but only stunned". — Humboldt-PN2
- "by degrees the impetuosity of this unequal combat diminished, and the wearied gymnoti dispersed." — Humboldt-PN2
- His own shock: "I do not remember having ever received from the discharge of a large Leyden jar, a more dreadful shock than that which I experienced by imprudently placing both my feet on a gymnotus just taken out of the water. I was affected during the rest of the day with a violent pain in the knees, and in almost every joint." — Humboldt-PN2
- A local belief: the eels "may be touched with impunity while you are chewing tobacco." — Humboldt-PN2
- Catania (2016): the story "has been recounted and illustrated in many publications, but subsequent investigators have been skeptical, and no similar eel behavior has been reported in more than 200 years. Here I report a defensive eel behavior that supports Humboldt's account." — Catania2016
- The leap: "the eel presses its chin against a threatening conductor while discharging high-voltage volleys", sending "increasing power… to the threat as the eel attains greater height". — Catania2016
- Found by accident with a metal-rimmed net: "the eel transitioned from a retreat to an explosive attack targeting the metal part of the net." — Catania2019
- Leaping higher is "turning up the 'volume' of its attack." — Catania2019
- On a human arm, a small eel's currents "peaked at 40-50 mA". "Apparently a strong offense is the eel's best defense." — Catania2017 (whether the arm was Catania's own is **UNCERTAIN**; the paper says "a human subject")
- "electric eels are air-breathers and they hold air in their mouths between breaths." — Catania2019
- "For one of the new species, we recorded a discharge of 860 V, well above 650 V previously cited for Electrophorus, making it the strongest living bioelectricity generator." — deSantana2019
- That species, *Electrophorus voltai*, is named "In honor of Alessandro Giuseppe Antonio Anastasio Volta (1745–1827)". — deSantana2019
- "Electric eels inspired the design of Volta's first electric battery". — deSantana2019
- They are knifefishes, not true eels: "the electric eel, Electrophorus electricus—a member of the Gymnotidae group". — Bray2022
- Sharks and rays "use specialized electrosensory organs called ampullae of Lorenzini to detect extremely small changes in environmental electric fields." — Bellono2017
- The platypus bill "is also an electroreceptive organ", sensitive to about "50 microV cm-1". — Scheich1986

## 20. A Rechargeable World (batteries, lithium-ion)

- The 2019 Chemistry Nobel was given "for the development of lithium-ion batteries", under the headline "They created a rechargeable world". — Nobel2019-PR
- Lithium was "created during the first minutes of the Big Bang". It "is the lightest solid element, which is why we hardly notice the mobile phones we now carry around." — Nobel2019-Pop
- Lithium "has just one electron in its outer electron shell, and this has a strong drive to leave lithium for another atom." — Nobel2019-Pop
- "in a battery, electrons should flow from the negative electrode – the anode – to the positive one – the cathode." — Nobel2019-Pop
- Whittingham's 1970s battery at Exxon "literally had great potential, just over two volts." — Nobel2019-Pop
- It kept catching fire: "The fire brigade had to put out a number of fires and finally threatened to make the laboratory pay for the special chemicals used to extinguish lithium fires." — Nobel2019-Pop
- An early customer was "a Swiss clockmaker that wanted to use it in solar-powered timepieces." — Nobel2019-Pop
- Goodenough, "in 1980 he demonstrated that cobalt oxide with intercalated lithium ions can produce as much as four volts." — Nobel2019-PR
- His insight: "batteries did not have to be manufactured in their charged state, as had been done previously. Instead, they could be charged afterwards." — Nobel2019-Pop
- Akira Yoshino "created the first commercially viable lithium-ion battery in 1985". — Nobel2019-PR
- Yoshino: "I just sort of sniffed out the direction that trends were moving. You could say I had a good sense of smell." — Nobel2019-Pop
- He "dropped a large piece of iron on the battery, but nothing happened". He called it "the moment when the lithium-ion battery was born". — Nobel2019-Pop
- Lithium-ion cells last because they rely on "lithium ions flowing back and forth between the anode and cathode", not reactions "that break down the electrodes". — Nobel2019-PR
- "Lithium-ion batteries have revolutionised our lives since they first entered the market in 1991." — Nobel2019-PR
- Goodenough "had significant problems learning to read" as a child. — Nobel2019-Pop
- He was the oldest Nobel laureate ever: "Awarded at age 97". — Nobel-Facts
- Born "25 July 1922, Jena, Germany"; died "25 June 2023, Austin, TX, USA", a month short of 101. (DERIVED from the dates.) — Nobel-Goodenough

## 21. Tiny Switches (semiconductors, briefly)

- In 1940 Russell Ohl found that impurities change silicon: "the element phosphorus, yielded a slight excess of electrons in the sample while the other, boron, led to a slight deficiency (later recognized as 'holes')." — CHM-1940
- "Ohl had discovered the photovoltaic effect that powers today's solar cells". — CHM-1940
- "On December 16, 1947, their research culminated in the first successful semiconductor amplifier": "two closely-spaced gold contacts held in place by a plastic wedge" on "a small slab of high-purity germanium". — CHM-1947
- "On December 23 they demonstrated their device to lab officials - in what Shockley deemed 'a magnificent Christmas present.'" — CHM-1947
- "Named the 'transistor' by electrical engineer John Pierce", it was announced publicly "on June 30, 1948". — CHM-1947
- Shockley, Bardeen and Brattain won the 1956 Physics Nobel "for their researches on semiconductors and their discovery of the transistor effect". — Nobel1956
- One phone-class chip (2020): "A14 Bionic is packed with 11.8 billion transistors". — Apple-A14

## 22. Electricity in Space (the ISS)

- "In 24 hours, the space station makes 16 orbits of Earth, traveling through 16 sunrises and sunsets." — NASA-ISS-Facts
- It moves at "a speed of five miles per second, orbiting Earth about every 90 minutes." — NASA-ISS-Facts
- "The acre of solar panels that power the station means sometimes you can look up in the sky at dawn or dusk and see the spaceship flying over your home". — NASA-ISS-Facts
- "Power Generation: 8 solar arrays provide 75 to 90 kilowatts of power". — NASA-ISS-Facts
- "The solar array wingspan (356 feet, 109 meters) is longer than the world's largest passenger aircraft, the Airbus A380". — NASA-ISS-Facts
- "Eight miles of wire connects the electrical power system aboard the space station." — NASA-ISS-Facts
- Each original array "is 112 feet long by 39 feet wide", and together they "require more than 250,000 silicon solar cells." — NASA-Glenn-EPS
- "The complete power system, consisting of U.S. and Russian hardware, generates 110 kilowatts (kW) total power, about as much as 55 houses would typically use." — NASA-Glenn-EPS
- "Earth will shadow the space station solar arrays from the sun for up to 36 minutes of each 92-minute orbit." — NASA-Glenn-EPS
- Power is distributed at "160 volts of direct current" and stepped down to 120 V DC. (The station runs on DC, Edison's kind.) — NASA-Glenn-EPS
- "The original set of batteries lasted almost 10 years (50,000 charge/discharge cycles) prior to replacement." — NASA-Glenn-EPS
- The upgrade finished in 2021 by "replacing 48 aging nickel-hydrogen batteries with 24 new lithium-ion batteries". — NASA-Blog-Batt
- New roll-out arrays (iROSA) "are 60 feet long by 20 feet wide". "Each new IROSA will produce more than 20 kilowatts of electricity, and once all are installed, will enable a 30% increase in power production". — NASA-Blog-iROSA23
- "Every spacecraft charges. It's just a question of whether it has a detrimental impact on the spacecraft or not." (Dr Joseph Minow) — NASA-NESC-Charging
- In 2010 the Galaxy 15 satellite charged up, and "much like walking across a carpet and then touching a door knob, an electrostatic discharge ensued that knocked out its communications systems". — NASA-NESC-Charging
- The station's path "takes it over 90 percent of the Earth's population". — NASA-ISS-Facts

## 23. Through-line: "If the electrons crawl, why does the light come on at once?"

Otto's question for the night, asked early while he watches a dark coast and a city switching on:
*"The electrons in a wire move slower than a snail. So why does the lamp light the instant you touch the switch?"*
Answer it in pieces through the video and finish it near the end.

- **1. They really are slow.** In house wiring at 20 A, drift is 4.54×10⁻⁴ m/s (OSX-9.2), about 37 minutes per metre (DERIVED). For a single bedside lamp, more like fifteen hours per metre (DERIVED). On AC they barely travel at all: they sway back and forth by a few hundred atoms' widths, fifty or sixty times a second (DERIVED).
- **2. The wire is already full.** "the electrons behave as an incompressible fluid… another leaves almost immediately, carrying the signal rapidly forward." — OSX-9.2
- **3. What travels is a change in the field.** "a rapidly propagating change in the electrical field due to equally rapid adjustments of surface charge" (OSX-9.2), moving "at essentially the speed of light" (HP-DRIFT).
- **4. The energy flows through the space around the wire.** "the electrons are getting their energy… because of the energy flowing into the wire from the field outside." — FEYN-II-27
- **5. The gentle ending:** "you find it impossible to flip off the light and get in bed before the room goes dark" (HP-DRIFT). The same Faraday lines of force (section 9), and the same Maxwell field that turned out to be light (section 10), carry the energy to the lamp. In a sense the lamp is lit by light's own cousin flowing round the outside of the wire.
- (Snail comparison: keep it qualitative. A specific snail speed is **UNCERTAIN/unsourced**.)

Alternative through-line (backup): *"Why does the night side of Earth glow?"* The answer is city lights, fishing boats, gas flares, auroras and airglow: "the Earth is never really dark" (NASA-EO-Black). It works well for an orbital narrator, but the first question has the more satisfying physics payoff.

## 24. Closing — gentle images and quotes to end on

- "The night is nowhere near as dark as most of us think. In fact, the Earth is never really dark." (Steven Miller, Colorado State University) — NASA-EO-Black
- "The night side of Earth twinkles with light. The first thing to stand out is the cities." — NASA-EO-Black
- "Wildfires and volcanoes rage. Oil and gas wells burn like candles. Auroras dance across the polar skies. Moonlight and starlight reflect off the water, snow, clouds, and deserts. Even the air and ocean sometimes glow." — NASA-EO-Black
- "'Nothing tells us more about the spread of humans across the Earth than city lights,' asserts Chris Elvidge, a NOAA scientist". — NASA-EO-Black
- The satellite sensor "can observe dim light down to the scale of an isolated highway lamp or fishing boat." — NASA-EO-Black
- The 2012 Black Marble "took satellite 312 orbits and 2.5 terabytes of data to get a clear shot of every parcel of Earth's land surface and islands." — NASA-BlackMarble
- Faraday: "There is no better, there is no more open door by which you can enter into the study of natural philosophy, than by considering the physical phenomena of a candle." — Faraday-Candle
- Faraday's last words to the children: "all I can say to you at the end of these lectures (for we must come to an end at one time or other) is to express a wish that you may, in your generation, be fit to compare to a candle; that you may, like it, shine as lights to those about you". — Faraday-Candle
- Volta on his pile: "on la touche, pour ainsi dire, des mains" [one touches it, so to speak, with one's hands]. — Volta1800
- Franklin, still puzzled in 1747: "a Manner that I can by no Means comprehend!" — FP-Jul1747
- Millikan: "Science walks forward on two feet, namely theory and experiment". — MIL-LECT
- Feynman: "it is clear that our ordinary intuitions are quite wrong." — FEYN-II-27
- Aurora: patches that "blink on and off repeatedly for hours, then they disappear as the sun rises in the east." — NOAA-SWPC-Aurora
- Mary Shelley: "When I placed my head on my pillow, I did not sleep, nor could I be said to think." (Use it as a smile, not the last line.) — Shelley1831
- Sixteen sunsets: "In 24 hours, the space station makes 16 orbits of Earth, traveling through 16 sunrises and sunsets." — NASA-ISS-Facts

---

## Human details

1. Thales is our first witness to amber, but only through later writers (Hippias, Aristotle, Diogenes Laertius). None of his own writing survives. — DL
2. Stephen Gray was a dyer, then a pensioner living at the Charterhouse almshouse. He was the first person to win the Copley Medal, and he won it twice. — Rice-Gray
3. Gray's first "wire" was packthread held up by silk loops in a friend's long gallery. When they swapped the silk for thin brass wire, the electricity leaked away and the experiment failed. — Priestley1775
4. The boy on the clothes-lines weighed 47 pounds 10 ounces with his clothes on. Brass leaf rose up to his face. — Gray1731
5. Kleist, a cathedral dean, got the first jar shock in 1745. Nobody he wrote to could repeat it, because he hadn't explained that you had to hold the bottle in your hand. — DSB-Kleist
6. Allamand found that only Bohemian glass worked, while "English glasses" did nothing. — Priestley1775
7. Nollet made 180 royal guardsmen jump at once in front of the king at Versailles. — Aber
8. Franklin tried to kill a Christmas turkey with electricity, knocked himself out instead, and asked his brother not to tell anyone. — FP-Turkey
9. Franklin openly admitted that he could not understand his own "miraculous Bottle". — FP-Jul1747
10. At Marly, an old soldier named Coiffier drew the first spark from a thundercloud. The whole village ran after their priest through a hailstorm, thinking Coiffier had been killed. — FP-Dalibard
11. Franklin told nobody but his son about the kite, "dreading the ridicule which too commonly attends unsuccessful attempts in science". — FP-Priestley
12. Galvani was a 54-year-old professor of obstetrics when his frog paper appeared. — Galvani
13. Volta wrote to London in French, from Como, on 20 March 1800. He said you could "touch" the endless current "with one's hands". — Volta1800
14. Napoleon used to look round the Institut and ask, "Where is Volta? Is he ill?" — Arago
15. Mary Shelley lay awake after a night of talk about galvanism, and *Frankenstein* began there. — Shelley1831
16. Ohm's father was a self-taught locksmith. Ohm himself was sent away from university for too much dancing, skating and billiards. — MACTUTOR-OHM
17. Ørsted's compass needle moved so little that the audience didn't notice. — APS-OER
18. Faraday's family was poor: as a boy he was given one loaf of bread to last a week. — BRIT-FAR
19. Faraday bound his own notes from Davy's lectures and sent them to Davy. He got the job when Davy's assistant was sacked for fighting. — BRIT-FAR
20. The first electric motor ran in a candle-lit basement on 3 September 1821. Faraday wrote, "Very satisfactory, but make more sensible apparatus". — RI-MOTOR
21. Faraday's induction ring was wound with wire "made for bonnets" and took about ten working days to make. — RI-RING
22. Faraday turned down the presidency of the Royal Society twice. — RI-FARADAY
23. J.J. Thomson called his particles "corpuscles". One listener thought he was "pulling their legs". — RI-JJT; APS-ELEC
24. Millikan's student, Harvey Fletcher, got the oil drops from a perfume atomizer. — APS-MIL
25. Tesla arrived in New York with "four cents in his pocket, a few of his own poems, and calculations for a flying machine." — Brit-Tesla
26. Edison switched on Pearl Street from J. P. Morgan's office. The *New York Times* reported it under "Miscellaneous City News". — ETHW-Pearl
27. Stanley hung his AC wires from the elm trees along Main Street in Great Barrington. — ETHW-Stanley
28. In 2018, oven clocks all over Europe ran about six minutes slow because of a political dispute in the Balkans. — ENTSOE-2018
29. The biggest kettle surge in British history (2,800 MW) came at the end of the 1990 penalty shoot-out. — NESO-Euro2020
30. Humboldt stepped on an electric eel with both feet and had sore knees for the rest of the day. — Humboldt-PN2
31. Whittingham's lab fires got so bad that the fire brigade threatened to send the lab a bill. — Nobel2019-Pop
32. As a child, Goodenough had serious trouble learning to read. He won the Nobel at 97. — Nobel2019-Pop; Nobel-Facts
33. Shockley called the first transistor "a magnificent Christmas present." — CHM-1947
34. Pilots described sprites for almost a century before anyone believed them. — NASA-Sprites
35. Andreas Mogensen filmed a blue jet while flying over the Bay of Bengal at 28,800 km/h. — ESA-ASIM

---

## UNCERTAIN — collected

1. **Musschenbroek's "kingdom of France" line:** this is Priestley's English paraphrase of a French letter to Réaumur, which we did not read, and Leiden University words it differently. Present it as "he wrote that…" in paraphrase. The date of the letter is not verified.
2. **Nollet's "200 Carthusian monks":** no source found. Leiden University says 700 monks. The 180 guardsmen are verified (Aber).
3. **Gray's "charity boy on silk cords":** Gray's own paper says only "a Boy", and says hair lines, not silk.
4. **Kleist's date "11 October 1745":** found only on Wikipedia. The verified dates are his letters of 4 Nov 1745 and December 1745.
5. **Dalibard's rod:** the primary report says 40 French feet, at Marly. APS says 50 ft "in Paris". Use the primary.
6. **Richmann's death date (6 Aug 1753, per Priestley):** the Julian vs Gregorian calendar question was not checked.
7. **The kite hoax claim (Tucker 2003):** a minority view. Franklin's own text is written as instructions; the first-person detail comes from Priestley (1767).
8. **Volta's Paris demonstration year (usually 1801) and the year he was made a count (1801 vs 1810):** the Arago scan is garbled and sources disagree.
9. **Forster/Aldini execution date (17 or 18 Jan 1803)** and lurid details: secondary or sensational. Keep it gentle or leave it out.
10. **Ohm and the "web of naked fancies":** no source found. MacTutor names Schultz and Pohl as his opponents but gives no quote.
11. **Ørsted's pamphlet being in Latin; 21 April 1820 as the exact lecture day:** APS gives the date; Britannica and ETHW say only "April 1820". The Latin claim is not on any fetched page.
12. **Ampère's exact September 1820 dates:** not on the pages we fetched.
13. **William Dance** as the customer who gave Faraday the Davy tickets: the RI says only "a Patron of the shop".
14. **"Just plain Michael Faraday":** unsourced. Don't use it.
15. **"What use is a newborn baby?" (Faraday):** apocryphal. There is no Faraday source, and even the 1783 Franklin version is questioned (Chapin 1985).
16. **Gladstone and "tax it":** first printed in 1899, second-hand, 32 years after Faraday's death (LECKY-1899).
17. **Hertz, "It's of no use whatsoever":** widely repeated but unsourced.
18. **Cable velocity factor of 0.6–0.9c:** the principle comes from Feynman (insulation slows the wave); the exact range has no fetched source. Say "most of the speed of light".
19. **"Slower than a snail":** fine as a picture, but no specific snail speed is sourced.
20. **Drift times per metre:** these are DERIVED by us from OpenStax's worked example. They are honest, but say "roughly".
21. **Faraday hired in 1813 (RI, APS) vs 1812 (Britannica); Christmas Lectures founded 1825 (RI) vs 1826 (ETHW):** we follow the RI.
22. **Harold P. Brown's role in the electric-chair campaign:** no fetched source names him. Say "supporters of DC".
23. **Tesla's AIEE lecture day (often 16 May 1888):** Martin's book says only "May, 1888".
24. **The Westinghouse–Tesla patent deal:** the month varies (May vs about July 1888) and no price was verified.
25. **Tesla tearing up his royalty contract:** ETHW itself says "supposedly".
26. **Tesla's $50,000 story and Edison's "you take the cake":** both come only from Tesla's own 1919 memoir.
27. **Why Europe uses 50 Hz:** no source fetched. North America's 60 Hz is linked to Tesla's motor (ETHW-Buffalo).
28. **"Sir Adam Beck No. 2" as the 1965 relay site:** the 2003 report says only "Beck" / "a generating plant in Ontario".
29. **People affected by the 2025 Iberian blackout (often 55–60 million):** not stated in the ENTSO-E reports we read.
30. **"People saw the Milky Way during the 2003 blackout" / LA 1994 "silvery sky" calls:** no reputable source found. Leave out, or say "people said".
31. **Edison's bulb burn time:** NPS says "at least 13 hours"; other figures (13.5, 14.5, 40 hours) vary.
32. **ISS power "240 kW" and "262,400 solar cells":** NOT confirmed. NASA says "75 to 90 kilowatts" (facts page) or 110 kW total (Glenn), and "more than 250,000" cells.
33. **Schumann resonance "7.83 Hz":** NASA says only "as low as 8 Hertz".
34. **Sprite duration:** NASA says about a thousandth of a second; one NSSL line says "a few seconds". Use NASA's figure.
35. **Exact day of the first sprite photo (4 or 6 July 1989):** NASA gives only "July of 1989".
36. **Lightning voltage:** both figures are NOAA, about 300 million V (NWS) vs 100 million to 1 billion (NSSL). Give a range.
37. **"About 30,000 K":** our conversion of NWS's 50,000 °F is roughly 28,000 K, often rounded to 30,000 K.
38. **Nerve speed "up to 120 m/s":** from a 2023 *Cureus* paper and a 2024 review citing Hursh (1939), not a major textbook. Fine as "up to about 120 metres a second".
39. **SA node 80–100 per minute:** this is its rate with no nerve control, not the normal resting heart rate.
40. **Catania shocked on "his own arm":** the papers say "a human subject". Say "a volunteer's arm" unless confirmed.
41. **Global flash rate:** 44 ± 5 per second (Christian 2003). NASA's older "about 50" is rounded.
42. **Body's total electrical power:** not found. Only the nervous system's roughly 20 W is sourced (PNAS feature).

---

## Resources for the description

- The Kite Experiment (Franklin's own 1752 text, with Priestley's account) — Papers of Benjamin Franklin, Yale/APS — https://franklinpapers.org/yale?vol=4&page=360a
- Dalibard, Report of an Experiment with Lightning (Marly, 1752) — Papers of Benjamin Franklin — https://franklinpapers.org/yale?vol=4&page=302a
- The History and Present State of Electricity (Priestley, 1775) — Internet Archive — https://archive.org/details/historyandprese00priegoog
- De Magnete (Gilbert, 1600; Mottelay translation) — Internet Archive — https://archive.org/details/williamgilbertof00gilb
- Volta's 1800 letter to Joseph Banks, Philosophical Transactions — Internet Archive (JSTOR Early Journal Content) — https://archive.org/details/jstor-107060
- Benjamin Franklin and the Kite Experiment — The Franklin Institute — https://www.fi.edu/benjamin-franklin/kite-key-experiment
- May 10, 1752: First Experiment to Draw Electricity from Lightning — American Physical Society — https://www.aps.org/publications/apsnews/200005/history.cfm
- Frankenstein: the real experiments that inspired the fictional science — Aberystwyth University — https://www.aber.ac.uk/en/news/archive/2018/10/title-218032-en.html
- Discovery of the electron (This Month in Physics History) — American Physical Society — https://www.aps.org/apsnews/2000/10/discovery-of-the-electron
- J.J. Thomson – Facts (Nobel Prize in Physics 1906) — NobelPrize.org — https://www.nobelprize.org/prizes/physics/1906/thomson/facts/
- Robert Millikan oil drop results — American Physical Society — https://www.aps.org/apsnews/2006/08/robert-millikan-oil-drop-results
- Ampere: Introduction (the 2019 redefinition) — NIST — https://www.nist.gov/si-redefinition/ampere-introduction
- Model of Conduction in Metals (drift velocity worked example) — OpenStax University Physics — https://openstax.org/books/university-physics-volume-2/pages/9-2-model-of-conduction-in-metals
- Microscopic View of Electric Current — HyperPhysics, Georgia State University — http://hyperphysics.phy-astr.gsu.edu/hbase/electric/miccur.html
- Field Energy and Field Momentum (Feynman Lectures Vol. II, ch. 27) — Caltech — https://www.feynmanlectures.caltech.edu/II_27.html
- Georg Simon Ohm — MacTutor, University of St Andrews — https://mathshistory.st-andrews.ac.uk/Biographies/Ohm/
- July 1820: Oersted & Electromagnetism — American Physical Society — https://www.aps.org/apsnews/2008/07/1820-oersted-electromagnetism
- Michael Faraday (1791–1867) — The Royal Institution — https://www.rigb.org/explore-science/explore/person/michael-faraday-1791-1867
- The birth of electric motion — The Royal Institution — https://www.rigb.org/explore-science/explore/blog/birth-electric-motion
- On Physical Lines of Force (Maxwell, 1861–62, full text) — Wikisource transcription — https://en.wikisource.org/wiki/On_Physical_Lines_of_Force
- Milestones: Pearl Street Station, 1882 — IEEE / ETHW — https://ethw.org/Milestones:Pearl_Street_Station,_1882
- Early Electrification of Buffalo (Niagara, Chicago 1893, 25 and 60 Hz) — IEEE / ETHW — https://ethw.org/Early_Electrification_of_Buffalo
- Milestones: Alternating Current Electrification, 1886 (Stanley) — IEEE / ETHW — https://ethw.org/Milestones:Alternating_Current_Electrification,_1886
- Electric Light and Power System — Thomas A. Edison Papers, Rutgers — https://edison.rutgers.edu/life-of-edison/inventions?view=article&id=532:electric-light-and-power-system&catid=91:inventions
- Topsy the Elephant Was a Victim of Her Captors, Not Thomas Edison — Smithsonian Magazine — https://www.smithsonianmag.com/smart-news/topsy-elephant-was-victim-her-captors-not-really-thomas-edison-180961611/
- Inertia and the Power Grid: A Guide Without the Spin — NREL / U.S. DOE — https://docs.nlr.gov/docs/fy20osti/73856.pdf
- Final Report on the August 14, 2003 Blackout — U.S.-Canada Power System Outage Task Force — https://www.energy.gov/sites/default/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
- 28 April 2025 Iberian Blackout (reports) — ENTSO-E — https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/
- Continuing frequency deviation… (the slow clocks of 2018) — ENTSO-E — https://www.entsoe.eu/news/2018/03/06/press-release-continuing-frequency-deviation-in-the-continental-european-power-system-originating-in-serbia-kosovo-political-solution-urgently-needed-in-addition-to-technical/
- Severe Weather 101: Lightning FAQ — NOAA National Severe Storms Laboratory — https://www.nssl.noaa.gov/education/svrwx101/lightning/faq/
- Where Are the Lightning Hotspots on Earth? — Bulletin of the American Meteorological Society — https://journals.ametsoc.org/view/journals/bams/97/11/bams-d-14-00193.1.xml
- Seeing Sprites — NASA (archived) — http://web.archive.org/web/20220825131452/https://www.nasa.gov/mission_pages/sunearth/news/seeing-sprites.html
- The Astonishing Behavior of Electric Eels (Catania, 2019) — Frontiers / PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC6646469/
- Personal Narrative, Vol. 2 (Humboldt; the horses and eels) — Project Gutenberg — https://www.gutenberg.org/ebooks/7014
- Popular information: Nobel Prize in Chemistry 2019 (lithium-ion) — NobelPrize.org — https://www.nobelprize.org/prizes/chemistry/2019/popular-information/
- 1947: Invention of the Point-Contact Transistor — Computer History Museum — https://www.computerhistory.org/siliconengine/invention-of-the-point-contact-transistor/
- International Space Station Facts and Figures — NASA — https://www.nasa.gov/international-space-station/space-station-facts-and-figures/
- Out of the Blue and Into the Black (Earth at night) — NASA Earth Observatory — https://science.nasa.gov/earth/earth-observatory/out-of-the-blue-and-into-the-black/
- The Chemical History of a Candle (Faraday) — Project Gutenberg — https://www.gutenberg.org/ebooks/14474

Books: Michael Faraday, *The Chemical History of a Candle* (1861); Joseph Priestley, *The History and Present State of Electricity* (1767); Nancy Forbes & Basil Mahon, *Faraday, Maxwell, and the Electromagnetic Field* (2014); Jill Jonnes, *Empires of Light: Edison, Tesla, Westinghouse, and the Race to Electrify the World* (2003); David Bodanis, *Electric Universe* (2005); Richard P. Feynman, *The Feynman Lectures on Physics*, Vol. II (free online at Caltech).
