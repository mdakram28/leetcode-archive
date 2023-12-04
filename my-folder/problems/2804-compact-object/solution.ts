type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
    if (Array.isArray(obj))
    {
        const ret = [];
        for (const key in obj) {
            const val = obj[key];
            if (val && typeof val == "object") {
                ret.push(compactObject(val));
            } else if (val) {
                ret.push(val);
            }
        }
        return ret;
    } else {
        const ret = {};
        for (const key in obj) {
            const val = obj[key];
            if (val && typeof val == "object") {
                ret[key] = compactObject(val);
            } else if (val) {
                ret[key] = val;
            }
        }
        return ret;
    }
};
