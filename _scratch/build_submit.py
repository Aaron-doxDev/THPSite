"""Build submit-manuscript.html using the brand head/header/footer."""
import re
from pathlib import Path

ROOT = Path(r"C:\Users\Aaron\THPSite")
SCRATCH = ROOT / "_scratch"

head_inner = (SCRATCH / "_head.html").read_text(encoding="utf-8")
header_block = (SCRATCH / "_header.html").read_text(encoding="utf-8")
footer_block = (SCRATCH / "_footer.html").read_text(encoding="utf-8")

# Update title and og:title for this page
head_inner = re.sub(
    r"<title>[^<]*</title>",
    "<title>Submit Your Manuscript – True Haven Press</title>",
    head_inner, count=1,
)
head_inner = re.sub(
    r'<meta property="og:title" content="[^"]*"\s*/?>',
    '<meta property="og:title" content="Submit Your Manuscript – True Haven Press" />',
    head_inner, count=1,
)
# Append link to styles.css so the form-specific CSS overrides WP defaults
head_inner = head_inner.rstrip() + '\n<link rel="stylesheet" href="styles.css">\n'

WEBHOOK_URL = "https://doxdev.app.n8n.cloud/webhook/thp-site-submit"

main_html = f'''
<section class="page-hero">
  <div class="hero-inner">
    <h1>Submit Your Manuscript</h1>
    <p class="hero-intro">Tell us about you and your book — we'll review every submission carefully.</p>
  </div>
</section>

<main id="submit-main" class="submit-main">
  <div class="container submit-container">

    <form id="submitForm"
          class="submit-form"
          action="{WEBHOOK_URL}"
          method="POST"
          enctype="multipart/form-data"
          novalidate>

      <p class="submit-intro">
        Required fields are marked with <span class="req-mark" aria-hidden="true">*</span>.
        Plan on a few minutes; you can attach your manuscript and proposal at the bottom.
      </p>

      <fieldset class="form-section">
        <legend>About You</legend>

        <div class="field">
          <label for="f-name">Name <span class="req-mark" aria-hidden="true">*</span></label>
          <input id="f-name" name="name" type="text" required autocomplete="name">
        </div>

        <div class="field">
          <label for="f-email">Email Address <span class="req-mark" aria-hidden="true">*</span></label>
          <input id="f-email" name="email" type="email" required autocomplete="email">
        </div>

        <div class="field">
          <label for="f-phone">Phone Number</label>
          <input id="f-phone" name="phone" type="tel" autocomplete="tel">
        </div>
      </fieldset>

      <fieldset class="form-section">
        <legend>About Your Book</legend>

        <div class="field">
          <label for="f-title">Book Title <span class="req-mark" aria-hidden="true">*</span></label>
          <input id="f-title" name="bookTitle" type="text" required>
        </div>

        <div class="field">
          <label for="f-pen">Pen Name <span class="req-mark" aria-hidden="true">*</span></label>
          <input id="f-pen" name="penName" type="text" required>
          <small class="field-hint">If you publish under your real name, enter it here too.</small>
        </div>

        <div class="field">
          <label for="f-fiction">Fiction or Nonfiction?</label>
          <select id="f-fiction" name="fictionOrNonfiction">
            <option value="">— Select —</option>
            <option value="Fiction">Fiction</option>
            <option value="Nonfiction">Nonfiction</option>
          </select>
        </div>

        <div class="field">
          <label for="f-genre">Genre?</label>
          <input id="f-genre" name="genre" type="text" placeholder="e.g. Thriller, Memoir, Self-help">
        </div>

        <div class="field">
          <label for="f-doctype">Document type you'll be submitting?</label>
          <select id="f-doctype" name="documentType">
            <option value="">— Select —</option>
            <option value="Word doc">Word doc</option>
            <option value="PDF">PDF</option>
          </select>
          <small class="field-hint">Word is preferred. PDFs require additional document preparation.</small>
        </div>
      </fieldset>

      <fieldset class="form-section">
        <legend>Editing &amp; Process</legend>

        <div class="field">
          <span class="label-as-block">Editing Types Needed?</span>
          <div class="checkbox-group">
            <label class="checkbox-row">
              <input type="checkbox" name="editingTypes" value="Uncertain"> Uncertain
            </label>
            <label class="checkbox-row">
              <input type="checkbox" name="editingTypes" value="Editing Platinum Package"> Editing Platinum Package
            </label>
            <label class="checkbox-row">
              <input type="checkbox" name="editingTypes" value="Editing Gold Package"> Editing Gold Package
            </label>
            <label class="checkbox-row">
              <input type="checkbox" name="editingTypes" value="Proofreading ONLY"> Proofreading ONLY
            </label>
          </div>
        </div>

        <div class="field">
          <label for="f-ai">If you used AI, which one and to what extent?</label>
          <textarea id="f-ai" name="aiUsage" rows="3" placeholder="e.g. ChatGPT for outline brainstorming only; manuscript itself is hand-written."></textarea>
        </div>
      </fieldset>

      <fieldset class="form-section">
        <legend>Files</legend>

        <div class="field">
          <label for="f-manuscript">Upload your manuscript here</label>
          <input id="f-manuscript" name="manuscript" type="file"
                 accept=".doc,.docx,.pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/pdf">
          <small class="field-hint">.doc, .docx, or .pdf — Word format strongly preferred.</small>
        </div>

        <div class="field">
          <label for="f-proposal">Upload your proposal here</label>
          <input id="f-proposal" name="proposal" type="file"
                 accept=".doc,.docx,.pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/pdf">
          <small class="field-hint">Optional. Especially helpful for nonfiction.</small>
        </div>
      </fieldset>

      <fieldset class="form-section">
        <legend>Anything Else?</legend>

        <div class="field">
          <label for="f-notes">Notes</label>
          <textarea id="f-notes" name="notes" rows="5" placeholder="Anything you'd like us to know."></textarea>
        </div>
      </fieldset>

      <div class="form-actions">
        <button type="submit" class="submit-btn">Submit</button>
        <p id="submitStatus" class="submit-status" role="status" aria-live="polite"></p>
      </div>
    </form>

  </div>
</main>

<script>
(function () {{
  const form = document.getElementById('submitForm');
  const btn = form.querySelector('.submit-btn');
  const status = document.getElementById('submitStatus');

  form.addEventListener('submit', async function (ev) {{
    ev.preventDefault();
    status.textContent = '';
    status.className = 'submit-status';

    // Native validity check
    if (!form.checkValidity()) {{
      form.reportValidity();
      return;
    }}

    btn.disabled = true;
    const originalLabel = btn.textContent;
    btn.textContent = 'Sending…';

    try {{
      const fd = new FormData(form);
      const res = await fetch(form.action, {{
        method: 'POST',
        body: fd,
      }});
      if (!res.ok) {{
        throw new Error('Server responded ' + res.status);
      }}
      status.textContent = 'Thanks — your submission was received. We\\'ll review it and get back to you soon.';
      status.classList.add('is-success');
      form.reset();
    }} catch (err) {{
      console.error('Submission failed:', err);
      status.textContent = 'Something went wrong sending your submission. Please email managingeditor@truehavenpress.com or try again in a moment.';
      status.classList.add('is-error');
    }} finally {{
      btn.disabled = false;
      btn.textContent = originalLabel;
    }}
  }});
}})();
</script>
'''

new_html = (
    '<!DOCTYPE html>\n'
    '<html lang="en">\n'
    '<head>'
    + head_inner +
    '</head>\n'
    '\n'
    '<body class="submit-page is-block-theme">\n'
    '<div class="wp-site-blocks">\n'
    + header_block + '\n\n'
    + main_html + '\n\n'
    + footer_block + '\n'
    '</div>\n'
    '</body>\n'
    '</html>\n'
)

(ROOT / "submit-manuscript.html").write_text(new_html, encoding="utf-8")
print(f"Wrote submit-manuscript.html ({len(new_html):,} bytes)")
