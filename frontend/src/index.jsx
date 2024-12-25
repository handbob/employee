import React from "react";
import ReatDOM from "react-dom/client";

import App from "./App";

import "./api/employee";

ReatDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
