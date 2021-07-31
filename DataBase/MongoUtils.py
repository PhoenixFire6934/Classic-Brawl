class MongoUtils:
    def insert_data(self, collection,  data):
        collection.insert_one(data)


    def update_document(self, collection, query, item, value):
        collection.update_one(query, { "$set": { item: value } })


    def update_all_documents(self, collection, query, item, value):
        collection.update_many(query, { "$set": { item: value } })


    def delete_document(self, collection, args):
        collection.delete_one(args)


    def delete_all_documents(self, collection, args):
        collection.delete_many(args)


    def load_document(self, collection, args):
        return collection.find_one(args)


    def load_all_documents(self, collection, args):
        doc_list = []
        cursor = collection.find(args)
        for document in cursor:
            doc_list.append(document)

        return doc_list

    def load_all_documents_sorted(self, collection, args, element):
        doc_list = []
        cursor = collection.find(args).sort(element)
        for document in cursor:
            doc_list.append(document)

        return doc_list
