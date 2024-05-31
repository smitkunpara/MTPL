let dragArea = document.querySelector(".drag-area");
let fileInput = dragArea.querySelector("input[type='file']");
let submitButton = document.querySelector("input[type='submit']");
let emailInput = document.querySelector(".emailinput");

let fileName = null;

submitButton.style.display = "none";
dragArea.addEventListener("click", function() {
  fileInput.click();
});
fileInput.addEventListener("change", function() {
  if (fileInput.files.length > 0) {
    let fileType = fileInput.files[0].type;
    if (fileType === "text/csv" || fileType === "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") {
      submitButton.style.display = "block";
      if (fileName === null) {
  fileName = document.createElement("p");
  fileName.className = "uploadtext"; 
  dragArea.appendChild(fileName);
}
      fileName.textContent = "Selected file: " + fileInput.files[0].name;
    } else {
      alert("Only CSV and XLSX files are allowed.");
      fileInput.value = "";
    }
  }
});

submitButton.addEventListener("click", function(event) {
  if (fileInput.files.length === 0) {
    event.preventDefault();
    alert("Please select a file.");
  }
});

const Toast = {
  init() {
    this.hideTimeout = null;
    this.el = document.createElement("div");
    this.el.className = "toast";
    document.body.appendChild(this.el);
  },
  show(message, state) {
    clearTimeout(this.hideTimeout);
    this.el.textContent = message;
    this.el.className = "toast toast--visible";
    if (state) {
      this.el.classList.add(`toast--${state}`);
    }
    this.hideTimeout = setTimeout(() => {
      this.el.classList.remove("toast--visible");
    }, 3000);
  }
};

document.addEventListener("DOMContentLoaded", () => Toast.init());
