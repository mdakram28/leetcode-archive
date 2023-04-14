/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    const t = typeof object;

    if (t === "number" || t === "boolean") return object.toString();

    if (object === null) return "null";

    // TODO: Escape characters
    if (t === "string") return '"' + object + '"';

    if (Array.isArray(object)) return "["+ object.map(jsonStringify).join(",") +"]";

    // console.log(object)
    return "{"+ 
        Object.keys(object)
            .map(key => jsonStringify(key) + ":" + jsonStringify(object[key]))
            .join(",") 
    +"}";
};