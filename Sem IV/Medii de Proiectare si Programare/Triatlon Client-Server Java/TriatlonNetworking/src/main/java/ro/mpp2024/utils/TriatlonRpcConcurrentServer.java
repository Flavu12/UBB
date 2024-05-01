package ro.mpp2024.utils;


import ro.mpp2024.rpcprotocol.TriatlonClientRpcReflectionWorker;
import ro.mpp2024.ITriatlonServices;

import java.net.Socket;


public class TriatlonRpcConcurrentServer extends AbsConcurrentServer {
    private ITriatlonServices triatlonServer;
    public TriatlonRpcConcurrentServer(int port, ITriatlonServices triatlonServer) {
        super(port);
        this.triatlonServer = triatlonServer;
        System.out.println("Chat- ChatRpcConcurrentServer");
    }

    @Override
    protected Thread createWorker(Socket client) {
       // ChatClientRpcWorker worker=new ChatClientRpcWorker(chatServer, client);
        TriatlonClientRpcReflectionWorker worker=new TriatlonClientRpcReflectionWorker(triatlonServer, client);

        Thread tw=new Thread(worker);
        return tw;
    }

    @Override
    public void stop(){
        System.out.println("Stopping services ...");
    }
}
