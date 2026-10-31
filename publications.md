---
layout: default
title: Publications
---

For an up-to-date list of Ugo Dal Lago's publications,
see also the [DBLP profile](https://dblp.org/pid/44/3105.html).

<div id="dblp-publications">
  Loading publications from DBLP...
</div>

<script>
(async function () {
  const container = document.getElementById("dblp-publications");

  try {
    const response = await fetch(
      "{{ '/publications.json' | relative_url }}"
    );

    if (!response.ok) {
      throw new Error("HTTP " + response.status);
    }

    const publications = await response.json();
    container.replaceChildren();

    let year = null;
    let list = null;

    for (const p of publications) {
      if (p.year !== year) {
        year = p.year;

        const heading = document.createElement("h2");
        heading.textContent = year;
        container.appendChild(heading);

        list = document.createElement("ul");
        container.appendChild(list);
      }

      const li = document.createElement("li");

      const authors = document.createElement("span");
      authors.textContent = (p.authors || []).join(", ") + ". ";
      li.appendChild(authors);

      const title = document.createElement("a");
      title.textContent = p.title || "";
      title.href = p.url || "https://dblp.org/pid/44/3105.html";
      li.appendChild(title);

      const details = [
        p.venue,
        p.volume,
        p.number ? "(" + p.number + ")" : "",
        p.pages ? "pp. " + p.pages : "",
        p.year
      ].filter(Boolean).join(", ");

      li.appendChild(document.createTextNode(". " + details + "."));
      list.appendChild(li);
    }

    if (!publications.length) {
      container.textContent = "No publications found.";
    }
  } catch (error) {
    console.error(error);
    container.textContent =
      "Unable to load publications at the moment.";
  }
})();
</script>