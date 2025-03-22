document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("fileInput");
    const uploadBtn = document.getElementById("uploadBtn");
    const extractedText = document.getElementById("extractedText");
    const copyBtn = document.getElementById("copyBtn");
    const downloadBtn = document.getElementById("downloadBtn");
    const printBtn = document.getElementById("printBtn");
    const toggleDarkMode = document.getElementById("toggleDarkMode");

    uploadBtn.addEventListener("click", function () {
        let file = fileInput.files[0];
        if (!file) {
            alert("Please select a file.");
            return;
        }

        let formData = new FormData();
        formData.append("file", file);

        fetch("/extract", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.text) {
                extractedText.value = data.text;
            } else {
                alert("Error: " + data.error);
            }
        });
    });

    copyBtn.addEventListener("click", function () {
        extractedText.select();
        document.execCommand("copy");
        alert("Copied to clipboard!");
    });

    downloadBtn.addEventListener("click", function () {
        let formData = new FormData();
        formData.append("text", extractedText.value);

        fetch("/download-pdf", {
            method: "POST",
            body: formData,
        }).then(response => response.blob())
          .then(blob => {
              let url = window.URL.createObjectURL(blob);
              let a = document.createElement("a");
              a.href = url;
              a.download = "extracted_text.pdf";
              document.body.appendChild(a);
              a.click();
              a.remove();
          });
    });

    printBtn.addEventListener("click", function () {
        window.print();
    });

    toggleDarkMode.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");
    });
});