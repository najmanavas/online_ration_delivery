// form styling
const forms = document.getElementsByTagName("form");

if (forms) {
  let formArray = Array.from(forms);
  formArray.forEach((form) => {
    Array.from(form).forEach((elem) => {
      switch (elem.tagName.toLowerCase()) {
        case "input":
          switch (elem.type.toLowerCase()) {
            case "check":
              elem.classList.add("form-check-input");
              break;

            default:
              elem.classList.add("form-control");
              break;
          }
          break;

        case "textarea":
          elem.classList.add("form-control");
          break;

        default:
          break;
      }
    });
    let labels = form.querySelectorAll("label");
    Array.from(labels).forEach((label) => {
      label.classList.add("form-label");
    });
  });
}