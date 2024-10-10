## System Prompt: File Cleaning Task for Lusófona Files

**Objective:**  
The primary task is to clean a collection of text files obtained through a web scraping process. These files, in both Portuguese and English, contain a mix of valuable content and repetitive, irrelevant information. The goal is to remove all non-essential sections while preserving the integrity of the content unique to each file.

**Key User Needs and Requests:**

1. **Content Preservation:**  
   - Ensure the retention of file-specific content that pertains directly to the title or headline of each file. This includes event details, research topics, or individual announcements.
   - Avoid deleting any text that could be perceived as the core information or subject matter specific to the file’s primary topic.

2. **Identifying Irrelevant Sections:**
   - Remove generic URLs and sections common across multiple files. These include basic navigation links, service portals (e.g., Moodle, Office 365), and contact details.
   - Eliminate blocks of text related to site-wide resources, academic service links, repeated header/footer information, social media links, and cookie or privacy notices.

3. **Regex Utilization:**
   - Apply regular expressions to reliably identify and eliminate unwanted sections in a manner that is both comprehensive and precise.
   - The regex patterns need to be robust enough to handle variations in these repeated sections across different files.

4. **Error Handling and Testing:**
   - Conduct testing across a subset of files to verify accuracy before applying changes to the entire dataset.
   - Maintain backups of original files to safeguard against any loss of valuable data due to overzealous cleaning.

5. **Output Specification:**
   - The final cleaned file should contain only the distinct information specific to that file’s title, adhering to the trimmed example provided by the user.
   - It is crucial that the output aligns with the users' expectations focusing on event details, contributors, and description narratives without clutter.

6. **Documentation and Reporting:**
   - Document the cleaning process, including regex patterns used and any adjustments made during testing. This ensures transparency and provides a basis for reproducing the results or refining the process in the future.

7. **Additional Notes:**
   - The user requires highly precise and thorough removal techniques due to the large quantity and structured nature of the repetitive content.

**Desired Outcome:**
Produce a streamlined dataset of files where every document is free from redundant and irrelevant information, focusing solely on meaningful and unique content to facilitate more accurate data analysis and interpretation.

---

Example: 

IN an EXAMPLE FILE LIKE THIS: 

"""
# Response for https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental

    : https://www.ulusofona.pt/en/ : https://www.filmeu.eu/
        Courses: https://www.ulusofona.pt/en/courses News: https://www.ulusofona.pt/en/news Research: https://investigacao.ulusofona.pt/en/ Events: https://www.ulusofona.pt/en/events Applications: https://www.ulusofona.pt/en/applications
      : https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
          PT: https://www.ulusofona.pt/noticias/sucesso-vs-saude-mental EN: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
          open menu close menu
        close : https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
        close menu : https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental

            New Courses

            Our Courses

                Bachelors: https://www.ulusofona.pt/en/bachelor
                Masters: https://www.ulusofona.pt/en/masters
                PhD: https://www.ulusofona.pt/en/phd
                Post Graduation: https://www.ulusofona.pt/en/post-graduation

            Academic Info

                Bachelors: https://www.ulusofona.pt/en/bachelor
                Masters: https://www.ulusofona.pt/en/masters
                PhD: https://www.ulusofona.pt/en/phd
                Post Graduation: https://www.ulusofona.pt/en/post-graduation

            Resources

                Bachelors: https://www.ulusofona.pt/en/bachelor
                Masters: https://www.ulusofona.pt/en/masters
                PhD: https://www.ulusofona.pt/en/phd
                Post Graduation: https://www.ulusofona.pt/en/post-graduation
              https://www.ulusofona.pt/logo/filmeu-big.png : https://www.filmeu.eu/
                * Homepage: https://www.ulusofona.pt/
                * eMail: http://email.ulusofona.pt/
                * NetPA: https://secretaria.virtual.ensinolusofona.pt
                * Moodle: https://moodle.ensinolusofona.pt/
                * Colibri: https://videoconf-colibri.zoom.us/account/
                * Avadoc: https://secure.ensinolusofona.pt/avadoc/
                * Collaborator Portal: https://colaborador.ensinolusofona.pt/mygiaf/Login.xhtml
                * Kuadro (Room Booking): https://www.ulusofona.pt/en/news/kuadro-space
                * Teacher Record: https://secure.ensinolusofona.pt/ficha_docente/f?p=123:LOGIN_DESKTOP::::::
                * Office 365: https://www.ulusofona.pt/en/services/office-365
                * Intranet: https://grupolusofona.sharepoint.com/sites/Click/

                Courses

                  * Bachelors: https://www.ulusofona.pt/en/undergraduate
                  * Integrated Masters: https://www.ulusofona.pt/en/integrated-masters
                  * Masters: https://www.ulusofona.pt/en/masters
                  * Erasmus Mundus Masters: https://www.ulusofona.pt/en/erasmus-mundus
                  * PhD: https://www.ulusofona.pt/en/phd
                  * Post-graduation: https://www.ulusofona.pt/en/post-graduation
                  * Lifelong Training: https://www.ulusofona.pt/formacao
                  * Lusófona X - Digital Academy: https://lusofona-x.pt/en/

                Lusófona University

                  * Academic Calendars: https://www.ulusofona.pt/en/calendars
                  * Open Positions: https://www.ulusofona.pt/en/open-positions
                  * Faculties and Schools: https://www.ulusofona.pt/en/faculties-and-schools
                  * Gender and diversity plan: https://www.ensinolusofona.pt/en/gender-and-diversity-plan
                  * Course Fees: https://www.ulusofona.pt/en/fees
                  * Reasons to Attend: https://razoes.ulusofona.pt/
                  * Quality: https://www.ulusofona.pt/en/qualidade
                  * About Us: https://www.ulusofona.pt/en/about
                  * Pay us a visit: https://ulusofona.typeform.com/to/ypj6qk
                  * Internal Reporting Channel: https://www.ulusofona.pt/en/internal-reporting-channel

                Facilities

                  * Campus: https://campus.ulusofona.pt/
                  * Contacts: https://www.ulusofona.pt/en/contacts
                  * Founding Entity: https://www.cofac.pt
                  * Lusófona in the World: https://www.ensinolusofona.pt/en/
                  * Lusófona 360º: https://vr360.ulusofona.pt/visitavirtual_EN/

                Teachers

                  * Avadoc: https://www.ulusofona.pt/avadoc
                  * Welcome: https://boasvindas.ulusofona.pt/
                  * Teaching Career: https://www.ulusofona.pt/en/documents?q=Career
                  * Directory: https://diretorio.ulusofona.pt/
                  * Scientific Employment: https://www.ulusofona.pt/en/open-positions/scientific-employment-and-research-grants
                  * Teacher's portal: https://secure.ensinolusofona.pt/ficha_docente/f?p=123:LOGIN_DESKTOP::::::
                  * Lusófona Mobile Teachers: https://www.ulusofona.pt/en/services/mobile-app-for-teachers
                  * Collaborator Portal: https://colaborador.ensinolusofona.pt/mygiaf/Login.xhtml

                Research

                  * Research Portal: https://research.ulusofona.pt/
                  * ReCiL - Scientific Repository: https://recil.ensinolusofona.pt/
                  * Scientific Journals: https://revistas.ulusofona.pt/
                  * Research Units: https://investigacao.ulusofona.pt/

                Resources

                  * Library: https://biblioteca.ulusofona.pt/
                  * Click - e-Learning Portal: https://www.ulusofona.pt/en/click
                  * Documents: https://www.ulusofona.pt/documents
                  * FAQ - Help Center: https://www.ulusofona.pt/en/faqs
                  * Welcome Guide: https://bemvindo.ulusofona.pt/
                  * Logos and Graphic Identity: https://www.ulusofona.pt/documentos?cat=3
                  * Lost and Found: https://www.ulusofona.pt/en/lost-and-found
                  * Regulations: https://www.ulusofona.pt/en/documents?cat=1
                  * Reshape: https://secure.ensinolusofona.pt/reshape/
                  * Services: https://www.ulusofona.pt/en/services
                  * Theses & Dissertations Standards: https://www.ulusofona.pt/media/normas-para-elaboracao-e-apresentacao-de-dissertacoes-e-teses.pdf

                International

                  * Brazilian Students: https://www.ulusofona.pt/en/international-students/brazilian-students
                  * International Students: https://www.ulusofona.pt/en/international-students
                  * FILMEU - European University: https://www.filmeu.eu/
                  * Student Mobility: https://www.ulusofona.pt/en/mobility

                Students

                  * Thesis Defenses Calendar: https://www.ulusofona.pt/en/theses
                  * Ensino Lusófona App: https://www.ulusofona.pt/en/services/mobile-app
                  * Students Card: https://www.ulusofona.pt/en/news/students-card
                  * Internships: https://eva.ulusofona.pt/
                  * Students: https://www.ulusofona.pt/en/student
                  * Special Educational Needs: https://www.ulusofona.pt/en/gaenee
                  * Employment portal: https://eva.ulusofona.pt/portal-de-emprego-universia/
                  * Student Advisor: https://www.ulusofona.pt/en/student-advisor
                  * Scholarships: https://www.ulusofona.pt/en/acao-social-escolar
                  * Advantages and Benefits: https://www.ensinolusofona.pt/pt/vantagens

                Community

                  * On Wednesdays in Lusófona: https://www.ulusofona.pt/en/event/as-quartas-na-lusofona-23-24
                  * Fernando Lopes Cinema: https://www.ulusofona.pt/cinema-fernando-lopes
                  * Building Knowledge: https://www.ulusofona.pt/en/building-knowledge
                  * Open Days: https://www.ulusofona.pt/en/open-days
                  * Senior School: https://escolasenior.ulusofona.pt/
                  * Summer School: https://escolaverao.ulusofona.pt/
                  * Veterinary Hospital - Appointmen: https://www.ulusofona.pt/en/news/appointments-veterinary-hospital-
                  * Lusófona Talks: https://www.ulusofona.pt/en/lusofona-talks
                  * Green Lusófona: https://www.ulusofona.pt/en/green-lusofona

                Media and Events

                  * Chronicles: https://www.ulusofona.pt/en/chronicles
                  * Lessons: https://www.ulusofona.pt/en/lessons
                  * Lusófona In The Media: https://www.ulusofona.pt/en/lusofona-in-the-media
                  * My Story - Testimonies: https://www.ulusofona.pt/en/testimonials
                  * News: https://www.ulusofona.pt/en/news
                  * Podcast - Direta Sem Café: https://www.ulusofona.pt/en/news/direta-sem-cafe-podcast-lusofona
          * Courses: https://www.ulusofona.pt/en/courses
          * News: https://www.ulusofona.pt/en/news
          * Research: https://investigacao.ulusofona.pt/en/
          * Events: https://www.ulusofona.pt/en/events
          * Applications: https://www.ulusofona.pt/en/applications
          * Courses: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Bachelors: https://www.ulusofona.pt/en/undergraduate
              + Integrated Masters: https://www.ulusofona.pt/en/integrated-masters
              + Masters: https://www.ulusofona.pt/en/masters
              + Erasmus Mundus Masters: https://www.ulusofona.pt/en/erasmus-mundus
              + PhD: https://www.ulusofona.pt/en/phd
              + Post-graduation: https://www.ulusofona.pt/en/post-graduation
              + Lifelong Training: https://www.ulusofona.pt/formacao
              + Lusófona X - Digital Academy: https://lusofona-x.pt/en/
          * Lusófona University: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Academic Calendars: https://www.ulusofona.pt/en/calendars
              + Open Positions: https://www.ulusofona.pt/en/open-positions
              + Faculties and Schools: https://www.ulusofona.pt/en/faculties-and-schools
              + Gender and diversity plan: https://www.ensinolusofona.pt/en/gender-and-diversity-plan
              + Course Fees: https://www.ulusofona.pt/en/fees
              + Reasons to Attend: https://razoes.ulusofona.pt/
              + Quality: https://www.ulusofona.pt/en/qualidade
              + About Us: https://www.ulusofona.pt/en/about
              + Pay us a visit: https://ulusofona.typeform.com/to/ypj6qk
              + Internal Reporting Channel: https://www.ulusofona.pt/en/internal-reporting-channel
          * Facilities: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Campus: https://campus.ulusofona.pt/
              + Contacts: https://www.ulusofona.pt/en/contacts
              + Founding Entity: https://www.cofac.pt
              + Lusófona in the World: https://www.ensinolusofona.pt/en/
              + Lusófona 360º: https://vr360.ulusofona.pt/visitavirtual_EN/
          * Teachers: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Avadoc: https://www.ulusofona.pt/avadoc
              + Welcome: https://boasvindas.ulusofona.pt/
              + Teaching Career: https://www.ulusofona.pt/en/documents?q=Career
              + Directory: https://diretorio.ulusofona.pt/
              + Scientific Employment: https://www.ulusofona.pt/en/open-positions/scientific-employment-and-research-grants
              + Teacher's portal: https://secure.ensinolusofona.pt/ficha_docente/f?p=123:LOGIN_DESKTOP::::::
              + Lusófona Mobile Teachers: https://www.ulusofona.pt/en/services/mobile-app-for-teachers
              + Collaborator Portal: https://colaborador.ensinolusofona.pt/mygiaf/Login.xhtml
          * Research: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Research Portal: https://research.ulusofona.pt/
              + ReCiL - Scientific Repository: https://recil.ensinolusofona.pt/
              + Scientific Journals: https://revistas.ulusofona.pt/
              + Research Units: https://investigacao.ulusofona.pt/
          * Resources: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Library: https://biblioteca.ulusofona.pt/
              + Click - e-Learning Portal: https://www.ulusofona.pt/en/click
              + Documents: https://www.ulusofona.pt/documents
              + FAQ - Help Center: https://www.ulusofona.pt/en/faqs
              + Welcome Guide: https://bemvindo.ulusofona.pt/
              + Logos and Graphic Identity: https://www.ulusofona.pt/documentos?cat=3
              + Lost and Found: https://www.ulusofona.pt/en/lost-and-found
              + Regulations: https://www.ulusofona.pt/en/documents?cat=1
              + Reshape: https://secure.ensinolusofona.pt/reshape/
              + Services: https://www.ulusofona.pt/en/services
              + Theses & Dissertations Standards: https://www.ulusofona.pt/media/normas-para-elaboracao-e-apresentacao-de-dissertacoes-e-teses.pdf
          * International: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Brazilian Students: https://www.ulusofona.pt/en/international-students/brazilian-students
              + International Students: https://www.ulusofona.pt/en/international-students
              + FILMEU - European University: https://www.filmeu.eu/
              + Student Mobility: https://www.ulusofona.pt/en/mobility
          * Students: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Thesis Defenses Calendar: https://www.ulusofona.pt/en/theses
              + Ensino Lusófona App: https://www.ulusofona.pt/en/services/mobile-app
              + Students Card: https://www.ulusofona.pt/en/news/students-card
              + Internships: https://eva.ulusofona.pt/
              + Students: https://www.ulusofona.pt/en/student
              + Special Educational Needs: https://www.ulusofona.pt/en/gaenee
              + Employment portal: https://eva.ulusofona.pt/portal-de-emprego-universia/
              + Student Advisor: https://www.ulusofona.pt/en/student-advisor
              + Scholarships: https://www.ulusofona.pt/en/acao-social-escolar
              + Advantages and Benefits: https://www.ensinolusofona.pt/pt/vantagens
          * Community: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + On Wednesdays in Lusófona: https://www.ulusofona.pt/en/event/as-quartas-na-lusofona-23-24
              + Fernando Lopes Cinema: https://www.ulusofona.pt/cinema-fernando-lopes
              + Building Knowledge: https://www.ulusofona.pt/en/building-knowledge
              + Open Days: https://www.ulusofona.pt/en/open-days
              + Senior School: https://escolasenior.ulusofona.pt/
              + Summer School: https://escolaverao.ulusofona.pt/
              + Veterinary Hospital - Appointmen: https://www.ulusofona.pt/en/news/appointments-veterinary-hospital-
              + Lusófona Talks: https://www.ulusofona.pt/en/lusofona-talks
              + Green Lusófona: https://www.ulusofona.pt/en/green-lusofona
          * Media and Events: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Chronicles: https://www.ulusofona.pt/en/chronicles
              + Lessons: https://www.ulusofona.pt/en/lessons
              + Lusófona In The Media: https://www.ulusofona.pt/en/lusofona-in-the-media
              + My Story - Testimonies: https://www.ulusofona.pt/en/testimonials
              + News: https://www.ulusofona.pt/en/news
              + Podcast - Direta Sem Café: https://www.ulusofona.pt/en/news/direta-sem-cafe-podcast-lusofona
          * eMail: http://email.ulusofona.pt/
          * NetPA: https://secretaria.virtual.ensinolusofona.pt
          * Moodle: https://moodle.ensinolusofona.pt/
          * Colibri: https://videoconf-colibri.zoom.us/account/
          * Avadoc: https://secure.ensinolusofona.pt/avadoc/
          * Collaborator Portal: https://colaborador.ensinolusofona.pt/mygiaf/Login.xhtml
          * Kuadro (Room Booking): https://www.ulusofona.pt/en/news/kuadro-space
          * Teacher Record: https://secure.ensinolusofona.pt/ficha_docente/f?p=123:LOGIN_DESKTOP::::::
          * Office 365: https://www.ulusofona.pt/en/services/office-365
          * Intranet: https://grupolusofona.sharepoint.com/sites/Click/
          Services
          WhatsApp - Oporto : https://api.whatsapp.com/send?phone=351961135355 netpa : https://secure.ensinolusofona.pt/ulht/secretaria_virtual/page?stage=netpahome&language=en Wifi : https://www.ulusofona.pt/en/services/wifi Moodle : https://moodle.ensinolusofona.pt/ Alterar password : https://secure.ensinolusofona.pt/alteracao_password/f?p=133:1:::::: Colibri : https://videoconf-colibri.zoom.us/account/ Office 365 : https://www.ulusofona.pt/en/services/office-365 WhatsApp - Lisbon : https://api.whatsapp.com/send?phone=351963640100
      https://www.ulusofona.pt/assets/images/cinema-logo.png : https://www.ulusofona.pt/en/cinema-fernando-lopes
        https://www.ulusofona.pt/images/sucesso-universidade-sem-deixar-vida_600.jpg

          Success Vs Mental Health

      NewsDetails

          With the participation of Dr. Mafalda Mascarenhas, PhD student in Social Psychology.

          10.11.22 - 11h35

            On October 12th at 3:30 pm, Dr. Mafalda Mascarenhas, PhD student in Social Psychology (LiSP, University of Lisbon) and author of the blog "Mind Researcher Diary", was at Lusófona University of Lisbon with the Political Science and International Relations class to talk about how to succeed at the University, without to have life.

            Dr. Mafalda tried to give some tips on how to have better school performance, being more attentive in class and making better use of the time spent in college, but at the same time she reminded us of the importance of having a good sleep, exercise routine and time to be with friends. and family. Another topic that has been increasingly discussed and that was also discussed in this presentation was Mental Health and its importance.

            In statements to the reporting team, the PhD student in Social Psychology confirmed that there was good interaction and sharing between all the students and states that all the topics discussed were very interesting.

                Share

                    Link Direto
          : https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental#share-modal

            Other News

                  * ULusófona Participates in the New Edition of Hospital da Bonecada: https://www.ulusofona.pt/en/news/ulusofona-participates-in-the-new-edition-of-hospital-da-bonecada
                  * ULusófona reinforces mental health support with psychology services on World Day: https://www.ulusofona.pt/en/news/ulusofona-reinforces-mental-health-support-with-psychology-services-on-world-day
                  * Lusófona University bets on automated customer service: https://www.ulusofona.pt/en/news/lusofona-university-bets-on-automated-customer-service
                  * ULusófona Promotes Scientific Research through CBIOS: https://www.ulusofona.pt/en/news/ulusofona-in-the-spotlight-through-cbios
                  * ULusófona Consultant Attends European Law Institute Congress: https://www.ulusofona.pt/en/news/ulusofona-consultant-attends-european-law-institute-congress
        Cookie Policy
          This site uses cookies to offer you a better browsing experience.
            Reject
            Choose >
            Allow All
              Necessary
            Necessary cookies for the operation of the website.
              Analytics
            Cookies for the purpose of analytics.
              Marketing
            Cookies for the purpose of advertisement.
            Reject
            Allow Selected
            Allow All

          Newsletter

            Subscription successful. Não foi possível adicionar o email à lista da newsletter.

      Subscribe to our Newsletter

      I agree with the privacy policy: https://www.ensinolusofona.pt/en/privacy-policy/ Subscribe
            * Facebook Porto: https://www.facebook.com/ulporto Lisboa: https://www.facebook.com/u.lusofona
            * X (Twitter) Porto: https://twitter.com/ulusofonaporto Lisboa: https://twitter.com/ulusofona
            * Threads Porto: https://www.threads.net/@ulporto Lisboa: https://www.threads.net/@ulusofona
          * Youtube : https://www.youtube.com/@UniversidadeLusofonaVideos
            * Instagram Porto: https://www.instagram.com/ulporto/ Lisboa: https://www.instagram.com/ulusofona/
            * Linkedin Porto: https://www.linkedin.com/school/universidade-lusofona-do-porto Lisboa: https://www.linkedin.com/school/universidade-lusofona-de-humanidades-e-tecnologias/

            Services

              * Contacts: https://www.ulusofona.pt/en/contacts
              * Password Change and Recovery: https://secure.ensinolusofona.pt/alteracao_password/f?p=133:2
              * Help us to improve: https://ulusofona.typeform.com/to/cipp2UFI
              * Lost and Found: https://www.ulusofona.pt/en/lost-and-found

            Courses

              * Bachelors: https://www.ulusofona.pt/en/undergraduate
              * Masters: https://www.ulusofona.pt/en/news/en/masters
              * PhD: https://www.ulusofona.pt/en/phd
              * Post-graduation: https://www.ulusofona.pt/en/post-graduation
              * All the courses: https://www.ulusofona.pt/en/courses

            Documents

              * Fees and Emoluments: https://www.ulusofona.pt/en/documents?cat=5
              * Regulations and Orders: https://www.ulusofona.pt/en/documents?cat=1
              * Forms: https://www.ulusofona.pt/en/documents?cat=13
              * Reports: https://www.ulusofona.pt/en/documents?cat=4
              * Validation of documents: https://www.ulusofona.pt/en/validation-of-issued-documents
            Lisboa
            Campo Grande, 376
            1749-024 Lisboa, Portugal
            Tel.: 217 515 500: tel:217515500 | email: info.cul@ulusofona.pt: mailto:info.cul@ulusofona.pt
            WhatsApp: +351 963 640 100: https://api.whatsapp.com/send?phone=351963640100
            Porto
            Rua Augusto Rosa, nº 24
            4000-098 Porto - Portugal
            Tel.: 222 073 230: tel:222073230 | email: info.cup@ulusofona.pt: mailto:info.cup@ulusofona.pt
            WhatsApp: +351 961 135 355: https://api.whatsapp.com/send?phone=351961135355
                2024 © COFAC | Privacy Policy: https://www.ensinolusofona.pt/en/privacy-policy
            https://www.ulusofona.pt/media/lisboa-2020.jpg https://www.ulusofona.pt/media/portugal-2020-small.jpg https://www.ulusofona.pt/media/financiado-eu-2024.png https://www.ulusofona.pt/media/prr-2024.png : https://recuperarportugal.gov.pt/ https://www.ulusofona.pt/media/republica-portuguesa-2024.png https://www.ulusofona.pt/media/logo-ue-financed.jpg https://www.ulusofona.pt/media/provedor-do-estudante.png : https://ulusofona.typeform.com/to/MTP9d7?typeform-source=www.ulusofona.pt https://www.ulusofona.pt/media/livro-de-reclamaoes.png : https://www.livroreclamacoes.pt/inicio https://www.ulusofona.pt/media/elogios.png : https://elogiar.livrodeelogios.com/elogiar/universidade-lusofona
"""

WE WANT TO DELETE ALL THIS IN QUOTE :

"""
 : https://www.ulusofona.pt/en/ : https://www.filmeu.eu/
        Courses: https://www.ulusofona.pt/en/courses News: https://www.ulusofona.pt/en/news Research: https://investigacao.ulusofona.pt/en/ Events: https://www.ulusofona.pt/en/events Applications: https://www.ulusofona.pt/en/applications
      : https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
          PT: https://www.ulusofona.pt/noticias/sucesso-vs-saude-mental EN: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
          open menu close menu
        close : https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
        close menu : https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental

            New Courses

            Our Courses

                Bachelors: https://www.ulusofona.pt/en/bachelor
                Masters: https://www.ulusofona.pt/en/masters
                PhD: https://www.ulusofona.pt/en/phd
                Post Graduation: https://www.ulusofona.pt/en/post-graduation

            Academic Info

                Bachelors: https://www.ulusofona.pt/en/bachelor
                Masters: https://www.ulusofona.pt/en/masters
                PhD: https://www.ulusofona.pt/en/phd
                Post Graduation: https://www.ulusofona.pt/en/post-graduation

            Resources

                Bachelors: https://www.ulusofona.pt/en/bachelor
                Masters: https://www.ulusofona.pt/en/masters
                PhD: https://www.ulusofona.pt/en/phd
                Post Graduation: https://www.ulusofona.pt/en/post-graduation
              https://www.ulusofona.pt/logo/filmeu-big.png : https://www.filmeu.eu/
                * Homepage: https://www.ulusofona.pt/
                * eMail: http://email.ulusofona.pt/
                * NetPA: https://secretaria.virtual.ensinolusofona.pt
                * Moodle: https://moodle.ensinolusofona.pt/
                * Colibri: https://videoconf-colibri.zoom.us/account/
                * Avadoc: https://secure.ensinolusofona.pt/avadoc/
                * Collaborator Portal: https://colaborador.ensinolusofona.pt/mygiaf/Login.xhtml
                * Kuadro (Room Booking): https://www.ulusofona.pt/en/news/kuadro-space
                * Teacher Record: https://secure.ensinolusofona.pt/ficha_docente/f?p=123:LOGIN_DESKTOP::::::
                * Office 365: https://www.ulusofona.pt/en/services/office-365
                * Intranet: https://grupolusofona.sharepoint.com/sites/Click/

                Courses

                  * Bachelors: https://www.ulusofona.pt/en/undergraduate
                  * Integrated Masters: https://www.ulusofona.pt/en/integrated-masters
                  * Masters: https://www.ulusofona.pt/en/masters
                  * Erasmus Mundus Masters: https://www.ulusofona.pt/en/erasmus-mundus
                  * PhD: https://www.ulusofona.pt/en/phd
                  * Post-graduation: https://www.ulusofona.pt/en/post-graduation
                  * Lifelong Training: https://www.ulusofona.pt/formacao
                  * Lusófona X - Digital Academy: https://lusofona-x.pt/en/

                Lusófona University

                  * Academic Calendars: https://www.ulusofona.pt/en/calendars
                  * Open Positions: https://www.ulusofona.pt/en/open-positions
                  * Faculties and Schools: https://www.ulusofona.pt/en/faculties-and-schools
                  * Gender and diversity plan: https://www.ensinolusofona.pt/en/gender-and-diversity-plan
                  * Course Fees: https://www.ulusofona.pt/en/fees
                  * Reasons to Attend: https://razoes.ulusofona.pt/
                  * Quality: https://www.ulusofona.pt/en/qualidade
                  * About Us: https://www.ulusofona.pt/en/about
                  * Pay us a visit: https://ulusofona.typeform.com/to/ypj6qk
                  * Internal Reporting Channel: https://www.ulusofona.pt/en/internal-reporting-channel

                Facilities

                  * Campus: https://campus.ulusofona.pt/
                  * Contacts: https://www.ulusofona.pt/en/contacts
                  * Founding Entity: https://www.cofac.pt
                  * Lusófona in the World: https://www.ensinolusofona.pt/en/
                  * Lusófona 360º: https://vr360.ulusofona.pt/visitavirtual_EN/

                Teachers

                  * Avadoc: https://www.ulusofona.pt/avadoc
                  * Welcome: https://boasvindas.ulusofona.pt/
                  * Teaching Career: https://www.ulusofona.pt/en/documents?q=Career
                  * Directory: https://diretorio.ulusofona.pt/
                  * Scientific Employment: https://www.ulusofona.pt/en/open-positions/scientific-employment-and-research-grants
                  * Teacher's portal: https://secure.ensinolusofona.pt/ficha_docente/f?p=123:LOGIN_DESKTOP::::::
                  * Lusófona Mobile Teachers: https://www.ulusofona.pt/en/services/mobile-app-for-teachers
                  * Collaborator Portal: https://colaborador.ensinolusofona.pt/mygiaf/Login.xhtml

                Research

                  * Research Portal: https://research.ulusofona.pt/
                  * ReCiL - Scientific Repository: https://recil.ensinolusofona.pt/
                  * Scientific Journals: https://revistas.ulusofona.pt/
                  * Research Units: https://investigacao.ulusofona.pt/

                Resources

                  * Library: https://biblioteca.ulusofona.pt/
                  * Click - e-Learning Portal: https://www.ulusofona.pt/en/click
                  * Documents: https://www.ulusofona.pt/documents
                  * FAQ - Help Center: https://www.ulusofona.pt/en/faqs
                  * Welcome Guide: https://bemvindo.ulusofona.pt/
                  * Logos and Graphic Identity: https://www.ulusofona.pt/documentos?cat=3
                  * Lost and Found: https://www.ulusofona.pt/en/lost-and-found
                  * Regulations: https://www.ulusofona.pt/en/documents?cat=1
                  * Reshape: https://secure.ensinolusofona.pt/reshape/
                  * Services: https://www.ulusofona.pt/en/services
                  * Theses & Dissertations Standards: https://www.ulusofona.pt/media/normas-para-elaboracao-e-apresentacao-de-dissertacoes-e-teses.pdf

                International

                  * Brazilian Students: https://www.ulusofona.pt/en/international-students/brazilian-students
                  * International Students: https://www.ulusofona.pt/en/international-students
                  * FILMEU - European University: https://www.filmeu.eu/
                  * Student Mobility: https://www.ulusofona.pt/en/mobility

                Students

                  * Thesis Defenses Calendar: https://www.ulusofona.pt/en/theses
                  * Ensino Lusófona App: https://www.ulusofona.pt/en/services/mobile-app
                  * Students Card: https://www.ulusofona.pt/en/news/students-card
                  * Internships: https://eva.ulusofona.pt/
                  * Students: https://www.ulusofona.pt/en/student
                  * Special Educational Needs: https://www.ulusofona.pt/en/gaenee
                  * Employment portal: https://eva.ulusofona.pt/portal-de-emprego-universia/
                  * Student Advisor: https://www.ulusofona.pt/en/student-advisor
                  * Scholarships: https://www.ulusofona.pt/en/acao-social-escolar
                  * Advantages and Benefits: https://www.ensinolusofona.pt/pt/vantagens

                Community

                  * On Wednesdays in Lusófona: https://www.ulusofona.pt/en/event/as-quartas-na-lusofona-23-24
                  * Fernando Lopes Cinema: https://www.ulusofona.pt/cinema-fernando-lopes
                  * Building Knowledge: https://www.ulusofona.pt/en/building-knowledge
                  * Open Days: https://www.ulusofona.pt/en/open-days
                  * Senior School: https://escolasenior.ulusofona.pt/
                  * Summer School: https://escolaverao.ulusofona.pt/
                  * Veterinary Hospital - Appointmen: https://www.ulusofona.pt/en/news/appointments-veterinary-hospital-
                  * Lusófona Talks: https://www.ulusofona.pt/en/lusofona-talks
                  * Green Lusófona: https://www.ulusofona.pt/en/green-lusofona

                Media and Events

                  * Chronicles: https://www.ulusofona.pt/en/chronicles
                  * Lessons: https://www.ulusofona.pt/en/lessons
                  * Lusófona In The Media: https://www.ulusofona.pt/en/lusofona-in-the-media
                  * My Story - Testimonies: https://www.ulusofona.pt/en/testimonials
                  * News: https://www.ulusofona.pt/en/news
                  * Podcast - Direta Sem Café: https://www.ulusofona.pt/en/news/direta-sem-cafe-podcast-lusofona
          * Courses: https://www.ulusofona.pt/en/courses
          * News: https://www.ulusofona.pt/en/news
          * Research: https://investigacao.ulusofona.pt/en/
          * Events: https://www.ulusofona.pt/en/events
          * Applications: https://www.ulusofona.pt/en/applications
          * Courses: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Bachelors: https://www.ulusofona.pt/en/undergraduate
              + Integrated Masters: https://www.ulusofona.pt/en/integrated-masters
              + Masters: https://www.ulusofona.pt/en/masters
              + Erasmus Mundus Masters: https://www.ulusofona.pt/en/erasmus-mundus
              + PhD: https://www.ulusofona.pt/en/phd
              + Post-graduation: https://www.ulusofona.pt/en/post-graduation
              + Lifelong Training: https://www.ulusofona.pt/formacao
              + Lusófona X - Digital Academy: https://lusofona-x.pt/en/
          * Lusófona University: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Academic Calendars: https://www.ulusofona.pt/en/calendars
              + Open Positions: https://www.ulusofona.pt/en/open-positions
              + Faculties and Schools: https://www.ulusofona.pt/en/faculties-and-schools
              + Gender and diversity plan: https://www.ensinolusofona.pt/en/gender-and-diversity-plan
              + Course Fees: https://www.ulusofona.pt/en/fees
              + Reasons to Attend: https://razoes.ulusofona.pt/
              + Quality: https://www.ulusofona.pt/en/qualidade
              + About Us: https://www.ulusofona.pt/en/about
              + Pay us a visit: https://ulusofona.typeform.com/to/ypj6qk
              + Internal Reporting Channel: https://www.ulusofona.pt/en/internal-reporting-channel
          * Facilities: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Campus: https://campus.ulusofona.pt/
              + Contacts: https://www.ulusofona.pt/en/contacts
              + Founding Entity: https://www.cofac.pt
              + Lusófona in the World: https://www.ensinolusofona.pt/en/
              + Lusófona 360º: https://vr360.ulusofona.pt/visitavirtual_EN/
          * Teachers: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Avadoc: https://www.ulusofona.pt/avadoc
              + Welcome: https://boasvindas.ulusofona.pt/
              + Teaching Career: https://www.ulusofona.pt/en/documents?q=Career
              + Directory: https://diretorio.ulusofona.pt/
              + Scientific Employment: https://www.ulusofona.pt/en/open-positions/scientific-employment-and-research-grants
              + Teacher's portal: https://secure.ensinolusofona.pt/ficha_docente/f?p=123:LOGIN_DESKTOP::::::
              + Lusófona Mobile Teachers: https://www.ulusofona.pt/en/services/mobile-app-for-teachers
              + Collaborator Portal: https://colaborador.ensinolusofona.pt/mygiaf/Login.xhtml
          * Research: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Research Portal: https://research.ulusofona.pt/
              + ReCiL - Scientific Repository: https://recil.ensinolusofona.pt/
              + Scientific Journals: https://revistas.ulusofona.pt/
              + Research Units: https://investigacao.ulusofona.pt/
          * Resources: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Library: https://biblioteca.ulusofona.pt/
              + Click - e-Learning Portal: https://www.ulusofona.pt/en/click
              + Documents: https://www.ulusofona.pt/documents
              + FAQ - Help Center: https://www.ulusofona.pt/en/faqs
              + Welcome Guide: https://bemvindo.ulusofona.pt/
              + Logos and Graphic Identity: https://www.ulusofona.pt/documentos?cat=3
              + Lost and Found: https://www.ulusofona.pt/en/lost-and-found
              + Regulations: https://www.ulusofona.pt/en/documents?cat=1
              + Reshape: https://secure.ensinolusofona.pt/reshape/
              + Services: https://www.ulusofona.pt/en/services
              + Theses & Dissertations Standards: https://www.ulusofona.pt/media/normas-para-elaboracao-e-apresentacao-de-dissertacoes-e-teses.pdf
          * International: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Brazilian Students: https://www.ulusofona.pt/en/international-students/brazilian-students
              + International Students: https://www.ulusofona.pt/en/international-students
              + FILMEU - European University: https://www.filmeu.eu/
              + Student Mobility: https://www.ulusofona.pt/en/mobility
          * Students: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Thesis Defenses Calendar: https://www.ulusofona.pt/en/theses
              + Ensino Lusófona App: https://www.ulusofona.pt/en/services/mobile-app
              + Students Card: https://www.ulusofona.pt/en/news/students-card
              + Internships: https://eva.ulusofona.pt/
              + Students: https://www.ulusofona.pt/en/student
              + Special Educational Needs: https://www.ulusofona.pt/en/gaenee
              + Employment portal: https://eva.ulusofona.pt/portal-de-emprego-universia/
              + Student Advisor: https://www.ulusofona.pt/en/student-advisor
              + Scholarships: https://www.ulusofona.pt/en/acao-social-escolar
              + Advantages and Benefits: https://www.ensinolusofona.pt/pt/vantagens
          * Community: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + On Wednesdays in Lusófona: https://www.ulusofona.pt/en/event/as-quartas-na-lusofona-23-24
              + Fernando Lopes Cinema: https://www.ulusofona.pt/cinema-fernando-lopes
              + Building Knowledge: https://www.ulusofona.pt/en/building-knowledge
              + Open Days: https://www.ulusofona.pt/en/open-days
              + Senior School: https://escolasenior.ulusofona.pt/
              + Summer School: https://escolaverao.ulusofona.pt/
              + Veterinary Hospital - Appointmen: https://www.ulusofona.pt/en/news/appointments-veterinary-hospital-
              + Lusófona Talks: https://www.ulusofona.pt/en/lusofona-talks
              + Green Lusófona: https://www.ulusofona.pt/en/green-lusofona
          * Media and Events: https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental
              + Chronicles: https://www.ulusofona.pt/en/chronicles
              + Lessons: https://www.ulusofona.pt/en/lessons
              + Lusófona In The Media: https://www.ulusofona.pt/en/lusofona-in-the-media
              + My Story - Testimonies: https://www.ulusofona.pt/en/testimonials
              + News: https://www.ulusofona.pt/en/news
              + Podcast - Direta Sem Café: https://www.ulusofona.pt/en/news/direta-sem-cafe-podcast-lusofona
          * eMail: http://email.ulusofona.pt/
          * NetPA: https://secretaria.virtual.ensinolusofona.pt
          * Moodle: https://moodle.ensinolusofona.pt/
          * Colibri: https://videoconf-colibri.zoom.us/account/
          * Avadoc: https://secure.ensinolusofona.pt/avadoc/
          * Collaborator Portal: https://colaborador.ensinolusofona.pt/mygiaf/Login.xhtml
          * Kuadro (Room Booking): https://www.ulusofona.pt/en/news/kuadro-space
          * Teacher Record: https://secure.ensinolusofona.pt/ficha_docente/f?p=123:LOGIN_DESKTOP::::::
          * Office 365: https://www.ulusofona.pt/en/services/office-365
          * Intranet: https://grupolusofona.sharepoint.com/sites/Click/
          Services
          WhatsApp - Oporto : https://api.whatsapp.com/send?phone=351961135355 netpa : https://secure.ensinolusofona.pt/ulht/secretaria_virtual/page?stage=netpahome&language=en Wifi : https://www.ulusofona.pt/en/services/wifi Moodle : https://moodle.ensinolusofona.pt/ Alterar password : https://secure.ensinolusofona.pt/alteracao_password/f?p=133:1:::::: Colibri : https://videoconf-colibri.zoom.us/account/ Office 365 : https://www.ulusofona.pt/en/services/office-365 WhatsApp - Lisbon : https://api.whatsapp.com/send?phone=351963640100
      https://www.ulusofona.pt/assets/images/cinema-logo.png : https://www.ulusofona.pt/en/cinema-fernando-lopes
        https://www.ulusofona.pt/images/sucesso-universidade-sem-deixar-vida_600.jpg
"""

AND ALSO DELETE THIS 

"""
Cookie Policy
          This site uses cookies to offer you a better browsing experience.
            Reject
            Choose >
            Allow All
              Necessary
            Necessary cookies for the operation of the website.
              Analytics
            Cookies for the purpose of analytics.
              Marketing
            Cookies for the purpose of advertisement.
            Reject
            Allow Selected
            Allow All

          Newsletter

            Subscription successful. Não foi possível adicionar o email à lista da newsletter.

      Subscribe to our Newsletter

      I agree with the privacy policy: https://www.ensinolusofona.pt/en/privacy-policy/ Subscribe
            * Facebook Porto: https://www.facebook.com/ulporto Lisboa: https://www.facebook.com/u.lusofona
            * X (Twitter) Porto: https://twitter.com/ulusofonaporto Lisboa: https://twitter.com/ulusofona
            * Threads Porto: https://www.threads.net/@ulporto Lisboa: https://www.threads.net/@ulusofona
          * Youtube : https://www.youtube.com/@UniversidadeLusofonaVideos
            * Instagram Porto: https://www.instagram.com/ulporto/ Lisboa: https://www.instagram.com/ulusofona/
            * Linkedin Porto: https://www.linkedin.com/school/universidade-lusofona-do-porto Lisboa: https://www.linkedin.com/school/universidade-lusofona-de-humanidades-e-tecnologias/

            Services

              * Contacts: https://www.ulusofona.pt/en/contacts
              * Password Change and Recovery: https://secure.ensinolusofona.pt/alteracao_password/f?p=133:2
              * Help us to improve: https://ulusofona.typeform.com/to/cipp2UFI
              * Lost and Found: https://www.ulusofona.pt/en/lost-and-found

            Courses

              * Bachelors: https://www.ulusofona.pt/en/undergraduate
              * Masters: https://www.ulusofona.pt/en/news/en/masters
              * PhD: https://www.ulusofona.pt/en/phd
              * Post-graduation: https://www.ulusofona.pt/en/post-graduation
              * All the courses: https://www.ulusofona.pt/en/courses

            Documents

              * Fees and Emoluments: https://www.ulusofona.pt/en/documents?cat=5
              * Regulations and Orders: https://www.ulusofona.pt/en/documents?cat=1
              * Forms: https://www.ulusofona.pt/en/documents?cat=13
              * Reports: https://www.ulusofona.pt/en/documents?cat=4
              * Validation of documents: https://www.ulusofona.pt/en/validation-of-issued-documents
            Lisboa
            Campo Grande, 376
            1749-024 Lisboa, Portugal
            Tel.: 217 515 500: tel:217515500 | email: info.cul@ulusofona.pt: mailto:info.cul@ulusofona.pt
            WhatsApp: +351 963 640 100: https://api.whatsapp.com/send?phone=351963640100
            Porto
            Rua Augusto Rosa, nº 24
            4000-098 Porto - Portugal
            Tel.: 222 073 230: tel:222073230 | email: info.cup@ulusofona.pt: mailto:info.cup@ulusofona.pt
            WhatsApp: +351 961 135 355: https://api.whatsapp.com/send?phone=351961135355
                2024 © COFAC | Privacy Policy: https://www.ensinolusofona.pt/en/privacy-policy
            https://www.ulusofona.pt/media/lisboa-2020.jpg https://www.ulusofona.pt/media/portugal-2020-small.jpg https://www.ulusofona.pt/media/financiado-eu-2024.png https://www.ulusofona.pt/media/prr-2024.png : https://recuperarportugal.gov.pt/ https://www.ulusofona.pt/media/republica-portuguesa-2024.png https://www.ulusofona.pt/media/logo-ue-financed.jpg https://www.ulusofona.pt/media/provedor-do-estudante.png : https://ulusofona.typeform.com/to/MTP9d7?typeform-source=www.ulusofona.pt https://www.ulusofona.pt/media/livro-de-reclamaoes.png : https://www.livroreclamacoes.pt/inicio https://www.ulusofona.pt/media/elogios.png : https://elogiar.livrodeelogios.com/elogiar/universidade-lusofona
"""

AND IN THE END THE NEW FILE MUST LOOK LIKE THIS (THIS IS WHAT WE CALL CONTENT OF THE FILE ):

"""
# Response for https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental

Success Vs Mental Health

      NewsDetails

          With the participation of Dr. Mafalda Mascarenhas, PhD student in Social Psychology.

          10.11.22 - 11h35

            On October 12th at 3:30 pm, Dr. Mafalda Mascarenhas, PhD student in Social Psychology (LiSP, University of Lisbon) and author of the blog "Mind Researcher Diary", was at Lusófona University of Lisbon with the Political Science and International Relations class to talk about how to succeed at the University, without to have life.

            Dr. Mafalda tried to give some tips on how to have better school performance, being more attentive in class and making better use of the time spent in college, but at the same time she reminded us of the importance of having a good sleep, exercise routine and time to be with friends. and family. Another topic that has been increasingly discussed and that was also discussed in this presentation was Mental Health and its importance.

            In statements to the reporting team, the PhD student in Social Psychology confirmed that there was good interaction and sharing between all the students and states that all the topics discussed were very interesting.

                Share

                    Link Direto
          : https://www.ulusofona.pt/en/news/sucesso-vs-saude-mental#share-modal

            Other News

                  * ULusófona Participates in the New Edition of Hospital da Bonecada: https://www.ulusofona.pt/en/news/ulusofona-participates-in-the-new-edition-of-hospital-da-bonecada
                  * ULusófona reinforces mental health support with psychology services on World Day: https://www.ulusofona.pt/en/news/ulusofona-reinforces-mental-health-support-with-psychology-services-on-world-day
                  * Lusófona University bets on automated customer service: https://www.ulusofona.pt/en/news/lusofona-university-bets-on-automated-customer-service
                  * ULusófona Promotes Scientific Research through CBIOS: https://www.ulusofona.pt/en/news/ulusofona-in-the-spotlight-through-cbios
                  * ULusófona Consultant Attends European Law Institute Congress: https://www.ulusofona.pt/en/news/ulusofona-consultant-attends-european-law-institute-congress
"""

THAT IS MUCH SHORTER AND ONLY ALMOST CONTAINS INFO ABOUT THE FILE TITLE 

IN THIS EXPLICIT EXAMPLE THE FILE WAS IN ENGLISH BUT YOU ALREADY SAW THE PORTUGUESE FILES AND IT'S ALMOST THE SAME EXCEPT THE TRANSLATION.

NOW KNOWING THIS CAN YOU BE MORE SPECIFIC AND EXPLICIT IN YOUR SUGESTIONS AND CODE SOLUTIONS? WE DON'T WE A PARAPHARED SOLUTION THAT DOENS'T WORK.. WE WANT A CLEAN AN DETAILED PLAN OR INFORMATION DO WE CAN ACTUALLY DO THIS WITH IMENSE PRECISION THAT WE MUST HAVE TO NOT LOSE VALEABLE DATA THAT WE CALL CONTENT OF THE FILE 