document.querySelector("#btn").addEventListener("click", () => {
  const txt = document.querySelector("#input").value;

  var request = document.createElement("div");
  var inputClasslist = ["card", "mb-3", "bg-primary", "text-white"];
  request.classList.add(...inputClasslist);
  request.style.maxWidth = "540px";
  var input = `
                    <div class="row no-gutters">
                      <div class="col-md-8">
                        <div class="card-body p-0">
                          <p class="card-text p-0 ml-3">
                            ${txt}
                          </p>
                          <p class="card-text"><small class="text-muted"></small></p>
                        </div>
                      </div>
                    </div>
                    `;
  request.innerHTML = input;
  document.querySelector(".messages").appendChild(request);

  // request url
  var url = `/myjsbot/${txt}`;
  console.log(url);
  var http = new XMLHttpRequest();

  http.open("GET", url, true);
  http.send();

  http.onload = function () {
    var div = document.createElement("div");
    if (this.status >= 200 && this.status < 300) {
      var classlist = ["card", "mb-3", "bg-success", "text-white", "ml-5"];
      div.classList.add(...classlist);
      div.style.maxWidth = "540px";
      var output = `
                    <div class="row no-gutters">
                      <div class="col-md-8">
                        <div class="card-body p-0">
                          <p class="card-text p-0 ml-3">
                            ${this.responseText}
                          </p>
                          <p class="card-text"><small class="text-muted"></small></p>
                        </div>
                      </div>
                    </div>
                    `;
      div.innerHTML = output;
      document.querySelector(".messages").appendChild(div);
    } else {
      console.log(this.status);
    }
  };
});
