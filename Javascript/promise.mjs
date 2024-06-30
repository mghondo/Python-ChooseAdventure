function doSomething(msg) {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      console.log(msg);
      resolve();
    }, 1000);
  });
}

function doSomething2(msg) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      try {
        throw new Error("bad error");
        console.log(msg);
        resolve();
      } catch (e) {
        reject(e);
      }
    }, 1000);
  });
}

export { doSomething, doSomething2 };
