**Objective**:
Transform web-scraped markdown documents into a clear, comprehensive representation of essential content. The focus is on extracting all valuable information, ensuring that the main content of the page is fully captured and presented. While filtering out repetitive and irrelevant text, ensure that the content length is preserved and formatted into a well-structured markdown format. Ensure the output reflects the true content, context, and structure of the original webpage, maintaining the same language as the input document.

---

**Instructions for the System**:

1. **Initial Header**:  
   - Begin each transformed output with: `"# Response for <url>"`, inserting the URL found in the file. This acts as a consistent identifier for the source of the content.

2. **Complete Core Content Identification and Extraction**:  
   - Ensure that all main content from the raw markdown file is thoroughly examined and extracted, maintaining the full content length.
   - This includes detailed articles, main text bodies, descriptions, and any substantial information.
   - Guarantee that all content of informational value is included; nothing should be omitted that contributes to the page's main message and context.

3. **Link Evaluation and Inclusion**:
   - **Preserve** links only if they provide significant relevance, additional details, or direct relevance to the core content.
   - **Exclude** links commonly found in navigation menus, headers, footers, or site-wide elements like terms of service and privacy policy unless directly relevant to the page content.

4. **Information Structure and Formatting**:
   - Employ markdown syntax to organize the output effectively, using headings, subheadings, lists, and bullet points to replicate the hierarchical and categorical structure of the original content.
   - Ensure that content flows logically and contextually, maintaining the essence and message of the source material.
   - Highlight and retain any contextually important links using markdown `[link text](URL)` format.

5. **Content Integrity and Verbosity**:
   - Keep the extracted content faithful to its original form without paraphrasing, ensuring a detailed representation that captures all essential information and nuances.
   - Deliver a verbose output that preserves the full length of the original content, presenting an accurate and immediately usable document.

6. **Quality and Consistency**:
   - Ensure precision and uniformity across outputs for different input files, respecting the specificity and uniqueness of each webpage’s content.
   - Pay strict attention to the details that characterize and define the content’s context and purpose.

7. **Language Consistency**:
   - Always produce the output in the same language as the raw input document to maintain linguistic accuracy and coherence.

---

**Content Processing Instructions**:

- **Pattern-based Noise Removal**:
  - Remove elements that are typically navigational or promotional, such as:
    - Menu items (e.g., "Cursos", "Notícias", "Investigação", "Eventos", "Candidaturas").
    - Links unrelated to the main topic like "Página Inicial", "Office 365", or "Moodle".
    - Social media links (e.g., "Facebook", "Twitter", "Instagram").
    - Administrative or utility links and text items (e.g., "Login", "Subscribe", "Newsletter").
    - Repeated elements like footers and standard disclaimers.

- **Focus Extraction**:
  - Concentrate on sections that exhibit clearly defined information, such as structured headings in the raw markdown that correlate with substantive text.

- **Link Relevance Check**:
  - Retain links that significantly enhance the content, disregarding generic site links unless directly tied to the primary content focus.

- **Content Authenticity**:
  - Preserve the authenticity and factual representation of the webpage’s information, ensuring it aligns with the original page's context and message.

---

**Reminder**: This prompt is a guideline designed to cover a wide variety of content while consistently achieving the objective of extracting and structuring meaningful information. Always adapt according to the unique characteristics presented within each file, ensuring completeness, full capture of the main content with its length preserved, and maintaining the original language.
