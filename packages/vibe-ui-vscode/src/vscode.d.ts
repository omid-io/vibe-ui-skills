declare module 'vscode' {
  export interface ExtensionContext {
    subscriptions: { push(item: any): void }[];
    extensionUri: Uri;
  }

  export interface Uri {
    fsPath: string;
  }

  export namespace Uri {
    export function parse(value: string): Uri;
  }

  export namespace window {
    export function registerWebviewViewProvider(viewId: string, provider: WebviewViewProvider): any;
    export function showWarningMessage(message: string): void;
    export function showErrorMessage(message: string): void;
    export function showInformationMessage(message: string): void;
    export function showQuickPick(items: any[], options?: any): Promise<any>;
    export const activeTextEditor: TextEditor | undefined;
  }

  export namespace commands {
    export function registerCommand(command: string, callback: (...args: any[]) => any): any;
  }

  export namespace env {
    export function openExternal(uri: Uri): Thenable<boolean>;
    export const clipboard: {
      writeText(text: string): Thenable<void>;
    };
  }

  export namespace workspace {
    export const workspaceFolders: { uri: Uri }[] | undefined;
  }

  export interface TextDocument {
    getText(): string;
  }

  export interface TextEditor {
    document: TextDocument;
    edit(callback: (editBuilder: any) => void): Thenable<boolean>;
  }

  export interface Webview {
    options: any;
    html: string;
    onDidReceiveMessage(callback: (message: any) => any): any;
  }

  export interface WebviewView {
    webview: Webview;
  }

  export interface WebviewViewResolveContext {}
  export interface CancellationToken {}

  export interface WebviewViewProvider {
    resolveWebviewView(
      webviewView: WebviewView,
      context: WebviewViewResolveContext,
      token: CancellationToken
    ): void;
  }
}
