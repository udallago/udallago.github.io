---
layout: default
title: Publications
---

<div id="dblp-publications">
  Loading publications...
</div>

<script>
(async function () {
  const container = document.getElementById("dblp-publications");

  try {
    const response = await fetch(
      "{{ '/publications.xml' | relative_url }}"
    );

    if (!response.ok) {
      throw new Error("HTTP " + response.status);
    }

    const xmlText = await response.text();
    const xml = new DOMParser().parseFromString(
      xmlText, "application/xml"
    );

    if (xml.querySelector("parsererror")) {
      throw new Error("Invalid XML");
    }

    const entries = Array.from(xml.querySelectorAll("r"));

    function cleanName(name) {
      return name.trim().replace(/\s+\d{4}$/, "");
    }

    const publications = entries.map(entry => {
      const item = entry.firstElementChild;

      function get(tag) {
        const el = item.querySelector(tag);
        return el ? el.textContent.trim() : "";
      }

      const authors = Array.from(
        item.querySelectorAll("author")
      ).map(a => cleanName(a.textContent));

      const editors = Array.from(
        item.querySelectorAll("editor")
      ).map(e => cleanName(e.textContent));

      return {
        year: get("year"),
        title: get("title"),
        authors: authors,
        editors: editors,
        venue: get("journal") || get("booktitle"),
        volume: get("volume"),
        number: get("number"),
        pages: get("pages"),
        url: get("ee") || get("url")
      };
    }).filter(p => p.venue !== "CoRR");

    publications.sort(
      (a, b) => Number(b.year) - Number(a.year)
    );

    container.replaceChildren();

    let currentYear = null;
    let list = null;

    for (const p of publications) {
      if (p.year !== currentYear) {
        currentYear = p.year;

        const heading = document.createElement("h2");
        heading.textContent = currentYear;
        container.appendChild(heading);

        list = document.createElement("ul");
        container.appendChild(list);
      }

      const li = document.createElement("li");

      // Autori oppure editor dei proceedings
      if (p.authors.length > 0) {
        li.appendChild(
          document.createTextNode(
            p.authors.join(", ") + ". "
          )
        );
      } else if (p.editors.length > 0) {
        const label = p.editors.length === 1
          ? " (editor). "
          : " (editors). ";

        li.appendChild(
          document.createTextNode(
            p.editors.join(", ") + label
          )
        );
      }

      // Titolo cliccabile
      const title = document.createElement("a");
      title.textContent = p.title;
      title.href = p.url || "https://dblp.org/pid/44/3105.html";
      li.appendChild(title);

      // Conferenza o journal in grassetto
      if (p.venue) {
        li.appendChild(document.createTextNode(". "));

        const venue = document.createElement("b");
        venue.textContent = p.venue;
        li.appendChild(venue);
      }

      // Dettagli bibliografici
      const details = [
        p.volume,
        p.number ? "(" + p.number + ")" : "",
        p.pages ? "pp. " + p.pages : "",
        p.year
      ].filter(Boolean).join(", ");

      if (details) {
        li.appendChild(
          document.createTextNode(", " + details + ".")
        );
      } else {
        li.appendChild(document.createTextNode("."));
      }

      list.appendChild(li);
    }

    if (!publications.length) {
      container.textContent = "No publications found.";
    }

  } catch (error) {
    console.error(error);
    container.textContent =
      "Unable to load publications.";
  }
})();
</script>
