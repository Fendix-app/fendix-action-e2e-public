const child_process = require("child_process");

function runJob(name) {
  return child_process.exec("run-job " + name);
}

module.exports = { runJob };
